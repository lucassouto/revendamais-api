import json
import requests
import re
import twitter
from config.settings.base import (API_KEY,
                                  API_SECRET,
                                  ACCESS_TOKEN,
                                  ACCESS_TOKEN_SECRET,
                                  FILE_WOEID)


class Twitter:
    api = twitter.Api(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    def trends(self, location=None):
        list_trends = []
        location_data = Woeid(FILE_WOEID)
        woeid = location_data.find_woeid(location)

        if woeid is not None:
            trends = self.api.GetTrendsWoeid(woeid=woeid)
            for i in range(10):
                list_trends.append(trends[i])

            return list_trends

        else:
            trends = self.api.GetTrendsCurrent()
            for i in range(10):
                list_trends.append(trends[i])

            return list_trends

    def search(self, term='', raw_query=None):
        if term != '':
            term = requests.utils.unquote(term)
        if raw_query is not None:
            raw_query = re.sub('[^a-zA-Z0-9=&_-]', '', raw_query)

        return self.api.GetSearch(term=term, count=20, raw_query=raw_query, return_json=True)

    def locations(self):
        with open(FILE_WOEID, 'r') as f:
            return json.load(f)


class Woeid:
    def __init__(self, file_name):
        with open(file_name, 'r') as f:
            self.data = json.load(f)

    def find_woeid(self, location):
        result = [x['woeid'] for x in self.data if x['name'] == location]

        if result != []:
            return result[0]
