djehuty
=======

post webhook manager written in Python

environment
-----------

- Python2.7 expected.

install
-------

You can use pip.

::

  $ pip install djehuty

create djehuty app on heroku
----------------------------

::

   $ pcreate -s djehuty_server YOUR_PROJECT_NAME
   $ cd YOUR_PROJECT_NAME
   $ git init
   $ heroku create

You can add existing services(slack only now)...::

  --- a/production.ini
  +++ b/production.ini
  @@ -8,6 +8,7 @@ pyramid.debug_routematch = false
   pyramid.default_locale_name = en
   pyramid.includes =
          djehuty
  +        djehutyslack

or implement your custom service in YOUR_PROJECT_NAME/YOUR_PROJECT_NAME/services.py.

implement custom service
------------------------

Example code with comments from djehutyslack<https://github.com/xica/djehutyslack/>.

.. code:: python

  # ..snipped..

  from djehuty.service import Service


  # inherit djehuty.service.Service.
  class Slack(Service):

      # add validation(authorization token, user credential, and so on) process.
      def validate(self, request):
          token = request.params.get('token')
          if not token or token != os.environ.get('DJEHUTY_SLACK_OUTGOING_TOKEN'):
              raise HTTPUnauthorized()

      # parse web hook request and return global argument for command.Command.app_args.
      def get_service_argument(self, name, request):
          if name == 'user':
              return request.params.get('user_name')
          elif name == 'room':
              return request.params.get('channel_name')
          else:
              raise ValueError('invalid argument name "{}"'.format(name))

      # parse web hook request and return "argv" list for app.App.run.
      def make_command_line(self, request):
          m = re.match(
              r'^{}\W*(.*)$'.format(request.params.get('trigger_word', '')),
              request.params.get('text', '')
          )
          return shlex.split(m.group(1).encode('utf8')) if m is not None else []

      # convert value returned by Command.take_action into appropriate response.
      def make_response(self, result):
          return {
              'text': result,
              'link_names': 1,
              'parse': 'full',
          }

  # explicit instantiation required.
  slack = Slack()

implement and add custom command
--------------------------------

djehuty.command.Command is a almost cliff<http://cliff.readthedocs.org/en/latest/> command.After implementing your command, add command name and command class module path in setup.py entry_points.

Example code with comments from djehuty.command.yo.

.. code:: python

  from djehuty.command import Command


  # inherit djehuty.command.Command.
  class Yo(Command):
      '''echo yo'''  # add description for help.

      # add argparse style argument and return parser.
      def get_parser(self, prog_name):
          parser = Command.get_parser(self, prog_name)
          parser.add_argument('-g', '--greeting',
                              default='yo',
                              help='greeting message')
          return parser

      # return response text.
      def take_action(self, parsed_args):
          return ('@{} '.format(self.app_args.user) if self.app_args.user else '') + parsed_args.greeting

todo
----

- Python 3 support
- unit test
