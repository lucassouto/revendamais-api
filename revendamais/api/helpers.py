import json
import twitter
from config.settings.base import (API_KEY,
                                  API_SECRET,
                                  ACCESS_TOKEN,
                                  ACCESS_TOKEN_SECRET,
                                  FILE_WOEID)


class Twitter:
    api = twitter.Api(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    def trends(self, location=None):
        location_data = Woeid(FILE_WOEID)
        woeid = location_data.find_woeid(location)

        if woeid is not None:
            return self.api.GetTrendsWoeid(woeid=woeid)
        else:
            return self.api.GetTrendsCurrent()

    def search(self, term):
        return self.api.GetSearch(term=term)


class Woeid:
    def __init__(self, file_name):
        with open(file_name, 'r') as f:
            self.data = json.load(f)

    def find_woeid(self, location):
        result = [x['woeid'] for x in self.data if x['name'] == location]

        if result != []:
            return result[0]
