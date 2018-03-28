class BotService(object):
    def __init__(self, telegramApiService, telegramUtilsService, pornHubService):
        self._telegramApiService = telegramApiService
        self._telegramUtilsService = telegramUtilsService
        self._pornHubService = pornHubService

    def handle_message(self, message):
        # print('On handle un message\n', message)
        self._telegramApiService.send_message(message['from']['id'], 'Hello, {}!'.format(message['from']['first_name']))

    def handle_inline_query(self, inline_query):
        # print('On handle un inline_query\n', inline_query, '\n\n')
        page = int(inline_query['offset']) if inline_query['offset'].isnumeric() else 1
        gifs, next_offset = self._pornHubService.search_gifs(inline_query['query'], page)
        results = self._telegramUtilsService.prepare_result_gifs(gifs)
        self._telegramApiService.answer_inline_query(inline_query['id'], results, next_offset)
