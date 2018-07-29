import os, sys
import random, string

class TelegramUtilsService(object):
    def __init__(self):
        pass

    def prepare_result_gifs(self, gifs):
        if os.getenv('ENVIRONMENT') == 'dev': sys.stdout.write('[DEBUG] Preparing {} GIFs for sending\n'.format(len(gifs)))

        results_gifs = []
        for gif in gifs:
            results_gifs.append({
                'type': 'gif',
                'id': ''.join([random.choice(string.ascii_letters) for _ in range(64)]),
                'gif_url': gif['gif_url'],
                'thumb_url': gif['poster_url'],
                'caption' : gif['source_video_url']
            })

        return results_gifs
