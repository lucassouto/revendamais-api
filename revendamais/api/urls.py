from django.urls import path
from .views import (
    LatestSearchesViewSet,
    TrendsViewSet,
    SearchViewSet,
    LocationsViewSet,
    SearchRawQueryViewSet,
)


list_actions = {"get": "list"}

single_actions = {"get": "retrieve"}

app_name = "api"
urlpatterns = [
    path(
        "latestsearches/",
        LatestSearchesViewSet.as_view(list_actions),
        name="latestsearches",
    ),
    path("trends/", TrendsViewSet.as_view(list_actions), name="trends"),
    path(
        "trends/<str:woeid>/",
        TrendsViewSet.as_view(single_actions),
        name="trends_woeid",
    ),
    path("search/<str:term>/", SearchViewSet.as_view(single_actions), name="search"),
    path(
        "search-raw-query/<str:raw_query>/",
        SearchRawQueryViewSet.as_view(single_actions),
        name="search_raw_query",
    ),
    path("locations/", LocationsViewSet.as_view(list_actions), name="locations"),
]
