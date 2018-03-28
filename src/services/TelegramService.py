import requests as r

class TelegramService(object):
    def __init__(self, api_token):
        self._api_token = api_token
        self._api_url = 'https://api.telegram.org/bot{}'.format(self._api_token)

    def send_message(self, target, text):
        print('On va envoyer "{}" a {}'.format(text, target))
        message = {
            'chat_id': target,
            'text': text
        }

        res = r.post(self._api_url + '/sendMessage', json=message)
        print(res.text)
        return True
