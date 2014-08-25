from djehuty.command import Command


class MyCommand(Command):
    '''sample command'''

    def get_parser(self, prog_name):
        parser = Command.get_parser(self, prog_name)
        parser.add_argument('-p', '--person',
                            default='djehuty',
                            help='person name')
        return parser

    def take_action(self, parsed_args):
        return 'hello {}'.format(parsed_args.person)
