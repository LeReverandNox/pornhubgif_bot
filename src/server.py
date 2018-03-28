import os, sys
if sys.version_info < (3, 6):
    exit("[ERR]: Please use Python 3.6 to run this bot.")

from dotenv import load_dotenv, find_dotenv; load_dotenv(find_dotenv())
# App
from bottle import Bottle
# Router
from router import Router
# Controllers
from controllers.BotController import *
# Services
from services.PornHubService import PornHubService
from services.TelegramApiService import TelegramApiService
from services.BotService import BotService

app = Bottle()

botService = BotService(TelegramApiService(os.getenv('TELEGRAM_API_TOKEN')), PornHubService())

controllers = {
    "botController": BotController(botService)
}

router = Router(app, controllers).register_routes()

app.run(host="localhost", port="8080", reloader=True)
