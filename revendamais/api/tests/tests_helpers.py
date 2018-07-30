from django.conf import settings
import twitter
from revendamais.api.helpers import Twitter, Woeid

API_KEY = settings.API_KEY
API_SECRET = settings.API_SECRET
ACCESS_TOKEN = settings.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = settings.ACCESS_TOKEN_SECRET
FILE_WOEID = settings.FILE_WOEID


class TestAPITwitter:
    def test_check_credentials(self):
        if (
            (API_KEY != "")
            and (API_SECRET != "")
            and (ACCESS_TOKEN != "")
            and (ACCESS_TOKEN_SECRET != "")
        ):
            assert True

    def test_api_verify_credentials(self):
        api = twitter.Api(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        verify = api.VerifyCredentials()

        assert verify is not None


class TestHelperTwitter:
    def test_trends(self):
        trends = Twitter().trends()

        assert trends != []

    def test_search_term(self):
        search = Twitter().search(term="lucassouto_1000")

        assert search is not None

    def test_search_raw_query(self):
        raw_query = "max_id=1022830329919365120&q=lucassouto_1000&count=20" \
                    "&include_entities=1&result_type=mixed"
        search = Twitter().search(raw_query=raw_query)

        assert search is not None

    def test_locations(self):
        locations = Twitter().locations()

        assert locations is not None


class TestWoeid:
    def test_check_json_woeid(self):
        if FILE_WOEID != '':
            assert True

    def test_get_woeid_location(self):
        result = Woeid(FILE_WOEID).find_woeid('Brazil')

        assert result is not None
