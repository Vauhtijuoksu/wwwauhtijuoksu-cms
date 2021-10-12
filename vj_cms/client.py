from datetime import datetime

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
        games = self.get('gamedata')
        for game in games:
            game['start_time'] = datetime.strptime(game['start_time'], '%Y-%m-%dT%H:%M:%SZ')
            game['end_time'] = datetime.strptime(game['end_time'], '%Y-%m-%dT%H:%M:%SZ')
        return games