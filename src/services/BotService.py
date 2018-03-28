class BotService(object):
    def __init__(self, telegramApiService, pornHubService):
        self._telegramApiService = telegramApiService
        self._pornHubService = pornHubService

    def handle_message(self, message):
        print('On handle un message\n', message)
        self._telegramApiService.send_message(message['from']['id'], 'Hello, {}!'.format(message['from']['first_name']))
        return True

    def handle_inline_query(self, inline_query):
        print('On handle un inline_query\n', inline_query, '\n\n')
        gifs = self._pornHubService.search_gifs(inline_query['query'])
        self._telegramApiService.answer_inline_query(inline_query['from']['id'], [])
        return True
