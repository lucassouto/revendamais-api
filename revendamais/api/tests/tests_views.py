from django.urls import reverse, resolve
from rest_framework.test import APIClient
import pytest
from revendamais.api.models import Searches
from revendamais.api.views import (
    LatestSearchesViewSet,
    LocationsViewSet,
    SearchRawQueryViewSet,
    SearchViewSet,
    TrendsViewSet,
)


def resolve_by_name(name, **kwargs):
    url = reverse(name, kwargs=kwargs)
    return resolve(url)


class TestLatestSearches:
    def test_resolves_list_url(self):
        resolver = resolve_by_name("api:latestsearches")
        assert resolver.func.cls == LatestSearchesViewSet


class TestTrends:
    def test_resolves_list_url(self):
        resolver = resolve_by_name("api:trends")
        assert resolver.func.cls == TrendsViewSet

    def test_resolves_retrieve_url(self):
        resolver = resolve_by_name("api:trends_woeid", woeid=1)
        assert resolver.func.cls == TrendsViewSet

    def test_resolves_url_to_list_action(self):
        resolver = resolve_by_name("api:trends")

        assert "list" == resolver.func.actions["get"]

    def test_resolves_url_to_retrieve_action(self):
        resolver = resolve_by_name("api:trends_woeid", woeid=1)

        assert "retrieve" == resolver.func.actions["get"]


class TestSearch:
    def test_resolves_list_url(self):
        resolver = resolve_by_name("api:search", term="lucassouto")
        assert resolver.func.cls == SearchViewSet

    def test_resolves_url_to_retrieve_action(self):
        resolver = resolve_by_name("api:search", term="lucassouto")

        assert "retrieve" == resolver.func.actions["get"]

    @pytest.mark.django_db
    def test_update_search(self):
        client = APIClient()
        search = Searches.objects.create(search="test_1")

        response = client.get("/api/v1/search/test_1/")
        x_search = Searches.objects.get(search="test_1")

        assert response.status_code == 200
        assert x_search.modified != search.modified


class TestSearchRawQuery:
    raw_query = "max_id=1022830329919365120&q=lucassouto_1000&count=20" \
                "&include_entities=1&result_type=mixed"

    def test_resolves_list_url(self):
        resolver = resolve_by_name("api:search_raw_query", raw_query=self.raw_query)
        assert resolver.func.cls == SearchRawQueryViewSet

    def test_resolves_url_to_retrieve_action(self):
        resolver = resolve_by_name("api:search_raw_query", raw_query=self.raw_query)

        assert "retrieve" == resolver.func.actions["get"]


class TestLocations:
    def test_resolves_list_url(self):
        resolver = resolve_by_name("api:locations")
        assert resolver.func.cls == LocationsViewSet
