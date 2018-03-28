
from typing import *
import bottle

class Router(object):
    def __init__(self, app: bottle.Bottle, controllers: Dict):
        self._app = app
        self._controllers = controllers

    def register_routes(self):
        print("On va register les routes")
        self._app.route('/', method='GET', callback=self._controllers["BotController"].helloworld)
