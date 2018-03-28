class BotController(object):
    def __init__(self, BotService):
        self._BotService = BotService
        print("Je suis le BotController")

    def helloworld(self):
        return 'Hello, World!'
