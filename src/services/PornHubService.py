import os, sys
import requests as r
from aiohttp import ClientSession
import asyncio
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
            anchor_elements = soup.select('li.gifVideoBlock a')

            poster_urls = [url for url in map(lambda element: element.video.attrs.get('poster'), anchor_elements)]
            video_urls = [url for url in map(lambda element: element.video.attrs.get('data-mp4'), anchor_elements)]
            gif_urls = [url for url in map(lambda url: url.replace('.mp4', '.gif'), video_urls)]
            page_urls = [url for url in map(lambda element: element.attrs.get('href'), anchor_elements)]

            loop = asyncio.get_event_loop()
            future = asyncio.ensure_future(self.get_gif_source_video_urls(page_urls))
            loop.run_until_complete(future)
            source_video_urls = future.result()

            gifs = [{'gif_url': gif_urls[i], 'video_url': video_urls[i], 'poster_url': poster_urls[i], 'source_video_url': source_video_urls[i]} for i in range(len(poster_urls))]

            if os.getenv('ENVIRONMENT') == 'dev': sys.stdout.write('[DEBUG] Found {} GIFs\n'.format(len(gifs)))
            return (gifs, page + 1)

        except Exception as e:
            sys.stderr.write("[ERR] Something went wrong during GIFs search : \n{}\n".format(e))
            return ([], 0)

    async def get_gif_source_video_url(self, session, gif_url):
        try:
            async with session.get(self._url + gif_url) as response:
                body = await response.read()
                soup = bs(body, 'html.parser')

                source_video_element = soup.select('.sourceTagDiv .bottomMargin a')[0]
                source_video_url = source_video_element.attrs.get('href')

                complete_video_url = self._url + source_video_url
                return complete_video_url
        except Exception as e:
            sys.stderr.write("[ERR] Something went wrong during GIFs video obtention for {} : \n{}\n".format(gif_url, e))
            return ""

    async def get_gif_source_video_urls(self, gif_urls):
        tasks = []

        async with ClientSession() as session:
            for url in gif_urls:
                task = asyncio.ensure_future(self.get_gif_source_video_url(session, url))
                tasks.append(task)

            responses = await asyncio.gather(*tasks)
            return responses
