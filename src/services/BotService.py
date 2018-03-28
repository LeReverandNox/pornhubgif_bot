class BotService(object):
    def __init__(self, telegramService, pornHubService):
        self._telegramService = telegramService
        self._pornHubService = pornHubService
