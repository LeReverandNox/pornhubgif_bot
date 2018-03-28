import random, string

class TelegramUtilsService(object):
    def __init__(self):
        pass

    def prepare_result_gifs(self, gifs):
        # print('On va preparer les gifs')
        results_gifs = []

        for gif in gifs:
            results_gifs.append({
                'type': 'gif',
                'id': ''.join([random.choice(string.ascii_letters) for _ in range(64)]),
                'gif_url': gif['gif_url'],
                'thumb_url': gif['gif_url'],
            })

        return results_gifs
