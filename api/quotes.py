import requests

class Quotes():
    enpoint = 'https://www.affirmations.dev/'

    def __init__(self):
        pass

    def run(self):
        request = requests.get(self.enpoint).json()
        return request['affirmation']
