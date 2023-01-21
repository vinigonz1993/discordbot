import requests
from config import CONFIG

class OCTranspo():
    enpoint = 'https://api.octranspo1.com/v2.0/GetNextTripsForStopAllRoutes'

    def __init__(self):
        APP_KEY = CONFIG['OCTRANSPO_APP_KEY']
        APP_ID = CONFIG['OCTRANSPO_APP_ID']
        self.url = f'{self.enpoint}?apiKey={APP_KEY}&appID={APP_ID}&format=json'

    def run(self, stopNo):
        request = requests.get(
            f'{self.url}&stopNo={stopNo}'
        ).json()

        return request