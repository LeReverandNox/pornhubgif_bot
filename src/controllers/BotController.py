from bottle import request, response

class BotController(object):
    def __init__(self, botService):
        self._botService = botService

    def helloworld(self):
        return {'message': 'Hello, World !'}
