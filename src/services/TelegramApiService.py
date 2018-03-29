import os, sys
import requests as r

class TelegramApiService(object):
    def __init__(self, api_token):
        self._api_token = api_token
        self._api_url = 'https://api.telegram.org/bot{}'.format(self._api_token)

    def send_message(self, target, text):
        if os.getenv('ENVIRONMENT') == 'dev': sys.stdout.write('[DEBUG] Sending message for chat_id={} and text={}\n'.format(target, text))

        payload = {
            'chat_id': target,
            'text': text
        }

        res = r.post(self._api_url + '/sendMessage', json=payload)
        if res.status_code != 200:
            sys.stdout.write("[WARN] Status-code {} on POST /sendMessage : \n{}\n".format(res.status_code, res.text))

    def answer_inline_query(self, target, results, next_offset):
        if os.getenv('ENVIRONMENT') == 'dev': sys.stdout.write('[DEBUG] Sending answer for inline query for inline_query__id={} and next_offset={}\n'.format(target, next_offset))

        payload = {
            'inline_query_id': target,
            'results': results,
            'next_offset': next_offset
        }

        res = r.post(self._api_url + '/answerInlineQuery', json=payload)
        if res.status_code != 200:
            sys.stdout.write("[WARN] Status-code {} on POST /answerInlineQuery : \n{}\n".format(res.status_code, res.text))
