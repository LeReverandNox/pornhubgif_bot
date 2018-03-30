import os, sys
if sys.version_info < (3, 6):
    exit("[ERR]: Please use Python 3.6 to run this bot.")

from dotenv import load_dotenv, find_dotenv; load_dotenv(find_dotenv())
# App
from bottle import Bottle
# Router
from Router import Router
# Controllers
from controllers.BotController import BotController
# Services
from services.PornHubService import PornHubService
from services.TelegramApiService import TelegramApiService
from services.TelegramUtilsService import TelegramUtilsService
from services.BotService import BotService
# PluginManager
from PluginManager import PluginManager

app = Bottle()

PluginManager(app).register_plugins().register_hooks()

botService = BotService(TelegramApiService(os.getenv('TELEGRAM_API_TOKEN')), TelegramUtilsService(), PornHubService())

controllers = {
    "botController": BotController(botService)
}

Router(app, controllers, os.getenv('TELEGRAM_API_TOKEN')).register_routes()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", quiet=True, reloader=True if os.getenv('ENVIRONMENT') == 'dev' else False)
