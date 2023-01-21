from config import CONFIG
import requests

class Exchange():
    endpoint = 'https://openexchangerates.org/api/latest.json'

    def __init__(self):
        EXCHANGE_APP_ID = CONFIG['EXCHANGE_APP_ID']
        self.url = f'{self.endpoint}?app_id={EXCHANGE_APP_ID}'

    def run(self):
        return requests.get(
            self.url
        ).json()
