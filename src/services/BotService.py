class BotService(object):
    def __init__(self, telegramApiService, pornHubService):
        self._telegramApiService = telegramApiService
        self._pornHubService = pornHubService

    def handle_message(self, message):
        print('On handle un message\n', message)
        self._telegramApiService.send_message(message['from']['id'], 'Hello, {}!'.format(message['from']['first_name']))
        return True

        self._telegramService.send_message(message['from']['id'], 'Hello, {}!'.format(message['from']['first_name']))
        return True
