import requests as r

class PornHubService(object):
    def __init__(self):
        self._url = "https://pornhub.com"

    def search_gifs(self, query):
        print('On va rechercher des gifs pour {}'.format(query))
        # Endpoint GET /gifs/search?search={}&page={}
