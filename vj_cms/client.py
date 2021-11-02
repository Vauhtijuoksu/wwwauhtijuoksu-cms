from datetime import datetime
from dateutil.parser import parse
import logging

from django.conf import settings

import requests
import requests_cache

requests_cache.install_cache(expire_after=60)

logger = logging.getLogger(__name__)

class VJClient:
    def __init__(self, base_url=None):
        if not base_url:
            base_url = settings.VJ_API_URL
        self.base_url = base_url.strip('/')

    def get(self, path):
        url = f'{self.base_url}/{path}'
        r = requests.get(url)
        if r.from_cache:
            logger.info(f'Using cached response for {url}')
        return r.json()

    def games(self):
        games = self.get('gamedata')
        for game in games:
            game['start_time'] = datetime.strptime(game['start_time'], "%Y-%m-%dT%H:%M:%S.%f%z")
            game['end_time'] = datetime.strptime(game['end_time'], "%Y-%m-%dT%H:%M:%S.%f%z")
        return games

    def donations(self):
        donations = self.get('donations')
        return donations


class LegacyClient(VJClient):
    def incentives(self):
        response = self.get('incentives')
        amounts = response['amount']

        game_dict = {}
        for i in response['incentives']:
            iid = str(i['id'])
            amount: dict = amounts.get(iid, {})
            if i['type'] in ['option', 'open']:
                if i['type'] == 'option':
                    options = [
                        {
                            'option': opt,
                            'amount': float(amount.get(str(opt_i + 1), 0))
                        } for opt_i, opt in enumerate(i['parameters'].split('/'))
                    ]
                else:
                    options = [
                        {
                            'option': opt,
                            'amount': float(amt)
                        } for opt, amt in amount.items()
                    ]
                options.sort(key=lambda opt: opt['amount'], reverse=True)
                total = sum(opt['amount'] for opt in options)
                if options:
                    max = options[0]['amount']
                else:
                    max = 0.0
            elif i['type'] == 'upgrade':
                options = []
                total = amount.get("null", 0.0)
                max = float(i['parameters'])

            i_dict = {
                'id': i['id'],
                'game': i['game'],
                'title': i['title'],
                'endtime': parse(i['endtime']),
                'type': i['type'],
                'parameters': i['parameters'],
                'info': i['info'],
                'total': total,
                'max': max,
                'options': options
            }
            game_incs = game_dict.get(i['game'], [])
            game_incs.append(i_dict)
            game_dict[i['game']] = game_incs

        return game_dict

