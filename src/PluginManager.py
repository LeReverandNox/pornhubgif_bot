from hooks.logger import logger_hook

class PluginManager(object):
    def __init__(self, app):
        self._app = app

    def register_plugins(self):
        return self

    def register_hooks(self):
        after_request_decorator = self._app.hook('after_request')
        after_request_decorator(logger_hook)

        return self
