class Router(object):
    def __init__(self, app, controllers):
        self._app = app
        self._controllers = controllers

    def register_routes(self):
        self._app.route('/webhook', method='POST', callback=self._controllers["botController"].post_webhook_action)
