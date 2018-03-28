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
from services.PornHubService import *
from services.TelegramService import *
from services.BotService import *

app = Bottle()

services = {
    "PornHubService": PornHubService(),
    "TelegramService": TelegramService(),
    "BotService": BotService()
}

controllers = {
    "BotController": BotController(services['BotService'])
}

router = Router(app, controllers)
router.register_routes()

app.run(host="localhost", port="8080", reloader=True)
