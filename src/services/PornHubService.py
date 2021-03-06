import os, sys
import requests as r
from bs4 import BeautifulSoup as bs

class PornHubService(object):
    def __init__(self):
        self._url = "https://pornhub.com"

    def search_gifs(self, query, page):
        if os.getenv('ENVIRONMENT') == 'dev': sys.stdout.write('[DEBUG] Searching GIFs on Pornhub for query={} and page={}\n'.format(query, page))

        try:
            if query:
                res = r.get(self._url + '/gifs/search?search={}&page={}'.format(query, page))
            else:
                res = r.get(self._url + '/gifs?page={}'.format(page))

            body = res.content
            soup = bs(body, 'html.parser')
            video_elements = soup.find_all('video', {'class': 'gifVideo'})

            poster_urls = [url for url in map(lambda element: element.attrs.get('data-poster'), video_elements)]
            video_urls = [url for url in map(lambda element: element.attrs.get('data-mp4'), video_elements)]
            gif_urls = [url for url in map(lambda url: url.replace('.mp4', '.gif'), video_urls)]

            gifs = [{'gif_url': gif_urls[i], 'video_url': video_urls[i], 'poster_url': poster_urls[i]} for i in range(len(poster_urls))]

            if os.getenv('ENVIRONMENT') == 'dev': sys.stdout.write('[DEBUG] Found {} GIFs\n'.format(len(gifs)))
            return (gifs, page + 1)

        except Exception as e:
            sys.stderr.write("[ERR] Something went wrong during GIFs search : \n{}\n".format(e))
            return ([], 0)
