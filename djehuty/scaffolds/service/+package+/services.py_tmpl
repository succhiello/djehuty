from djehuty.service import Service


class Myservice(Service):

    def validate(self, request):
        pass

    def get_service_argument(self, name, request):
        return ''

    def make_command_line(self, request):
        return ['mycommand', '-u', 'djehuty']

    def make_response(self, result):
        return {'body': result}


my_service = Myservice()
