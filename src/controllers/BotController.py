from bottle import request, response

class BotController(object):
    def __init__(self, botService):
        self._botService = botService

    def post_webhook_action(self):
        # print('On recoit un hit sur POST /webhook')
        try:
            payload = request.json
        except Exception as e:
            print('[ERR] Non-JSON payload received : \n{}'.format(e))
            response.status = 500
            return {'message': 'Please send me a JSON payload'}

        if not payload:
            response.status = 500
            return {'message': 'Please send me something in the payload'}

        # print('**** PAYLOAD ***')
        # print(payload)
        # print('****\n\n')
        if 'inline_query' in payload:
            self._botService.handle_inline_query(payload['inline_query'])
        if 'message' in payload:
            self._botService.handle_message(payload['message'])

        return ''
