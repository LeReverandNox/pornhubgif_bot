class Router(object):
    def __init__(self, app, controllers, api_token):
        self._app = app
        self._controllers = controllers
        self._short_api_token = api_token[10:]

    def register_routes(self):
        self._app.route('/webhook' + self._short_api_token, method='POST', callback=self._controllers["botController"].post_webhook_action)
