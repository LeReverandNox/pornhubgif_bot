import requests as r

class TelegramApiService(object):
    def __init__(self, api_token):
        self._api_token = api_token
        self._api_url = 'https://api.telegram.org/bot{}'.format(self._api_token)

    def send_message(self, target, text):
        # print('On va envoyer "{}" a {}'.format(text, target))
        payload = {
            'chat_id': target,
            'text': text
        }

        res = r.post(self._api_url + '/sendMessage', json=payload)
        # print(res.text)

    def answer_inline_query(self, target, results, next_offset):
        # print('On va envoyer "{}" a {}'.format([], target))
        payload = {
            'inline_query_id': target,
            'results': results,
            'next_offset': next_offset
        }

        res = r.post(self._api_url + '/answerInlineQuery', json=payload)
        # print(res.text)
