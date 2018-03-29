import os
import requests as r
from bs4 import BeautifulSoup as bs

class PornHubService(object):
    def __init__(self):
        self._url = "https://pornhub.com"

    def search_gifs(self, query, page):
        if os.getenv('ENVIRONMENT') == 'dev': print('[DEBUG] Searching GIFs on Pornhub for query={} and page={}'.format(query, page))

        try:
            res = r.get(self._url + '/gifs/search?search={}&page={}'.format(query, page))
            body = res.content
            soup = bs(body, 'html.parser')
            video_elements = soup.find_all('video', {'class': 'gifVideo'})

            poster_urls = [url for url in map(lambda element: element.attrs.get('poster'), video_elements)]
            video_urls = [url for url in map(lambda element: element.attrs.get('data-mp4'), video_elements)]
            gif_urls = [url for url in map(lambda url: url.replace('.mp4', '.gif'), video_urls)]

            gifs = [{'gif_url': gif_urls[i], 'poster_url': poster_urls[i]} for i in range(len(poster_urls))]

            if os.getenv('ENVIRONMENT') == 'dev': print('[DEBUG] Found {} GIFs'.format(len(gifs)))
            return (gifs, page + 1)

        except Exception as e:
            print("[ERR] Something went wrong during GIFs search : \n{}".format(e))
            return ([], 0)
