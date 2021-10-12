from django.conf import settings
import requests


class VJClient:
    def __init__(self, base_url=None):
        if not base_url:
            base_url = settings.VJ_API_URL
        self.base_url = base_url.strip('/')

    def get(self, path):
        url = f'{self.base_url}/{path}'
        r = requests.get(url)
        return r.json()

    def games(self):
        return self.get('gamedata')
