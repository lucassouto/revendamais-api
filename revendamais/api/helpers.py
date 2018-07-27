from config.settings.base import (API_KEY,
                                  API_SECRET,
                                  ACCESS_TOKEN,
                                  ACCESS_TOKEN_SECRET)
import twitter


class Twitter:
    api = twitter.Api(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    def trends(self):
        return self.api.GetTrendsCurrent()

    def search(self, term):
        return self.api.GetSearch(term=term)
