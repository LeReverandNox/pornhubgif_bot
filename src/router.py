
from typing import *
import bottle

class Router(object):
    def __init__(self, app: bottle.Bottle, controllers: Dict):
        self._app = app
        self._controllers = controllers

    def register_routes(self):
        self._app.route('/webhook', method='POST', callback=self._controllers["botController"].post_webhook_action)
