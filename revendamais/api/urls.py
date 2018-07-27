from django.urls import path
from .views import LatestSearchesViewSet, TrendsViewSet, SearchViewSet


list_actions = {
    'get': 'list'
}

app_name = 'api'
urlpatterns = [
    path('latestsearches/',
         LatestSearchesViewSet.as_view(list_actions),
         name="latestsearches"),

    path('trends/',
         TrendsViewSet.as_view(list_actions),
         name="trends"),

    path('search/<str:search>',
         SearchViewSet.as_view(list_actions),
         name="search"),
]
