import requests
from config import CONFIG

class WeatherApi():
    endpoint = 'https://api.openweathermap.org/data/2.5/weather'

    def __init__(self):
        WEATHER_API_KEY = CONFIG['WEATHER_API_KEY']
        self.url = f'{self.endpoint}?APPID={WEATHER_API_KEY}'

    def mount_qp(self, location, country):
        return f'&q={location},{country.lower()}'

    def run(self, location, country):
        qp = self.mount_qp(location, country)
        request = requests.get(
            f'{self.url}{qp}'
        ).json()

        return request
