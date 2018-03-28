class BotService(object):
    def __init__(self, telegramService, pornHubService):
        self._telegramService = telegramService
        self._pornHubService = pornHubService

    def handle_message(self, message):
        print('On handle un message\n', message)
        self._telegramService.send_message(message['from']['id'], 'Hello, {}!'.format(message['from']['first_name']))
        return True
