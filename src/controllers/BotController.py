import os, sys
from bottle import request, response

class BotController(object):
    def __init__(self, botService):
        self._botService = botService

    def post_webhook_action(self):
        try:
            payload = request.json
        except Exception as e:
            response.status = 500
            return {'message': 'Please send me a JSON payload'}

        if not payload:
            response.status = 500
            return {'message': 'Please send me something in the payload'}

        if os.getenv('ENVIRONMENT') == 'dev': sys.stdout.write('[DEBUG] Incoming payload : \n{}\n'.format(payload))

        if 'inline_query' in payload:
            self._botService.handle_inline_query(payload['inline_query'])
        elif 'message' in payload:
            self._botService.handle_message(payload['message'])

        return ''
