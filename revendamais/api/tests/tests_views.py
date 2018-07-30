from django.urls import reverse, resolve
from revendamais.api.views import LatestSearchesViewSet


class TestLatestSearches:
    def resolve_by_name(self, name, **kwargs):
        url = reverse(name, kwargs=kwargs)
        return resolve(url)

    def test_resolves_list_url(self):
        resolver = self.resolve_by_name("api:latestsearches")
        assert resolver.func.cls, LatestSearchesViewSet
