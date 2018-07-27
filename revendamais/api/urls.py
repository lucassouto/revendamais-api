from django.urls import path
from .views import LatestSearchesViewSet, Trends


list_actions = {
    'get': 'list'
}

app_name = 'api'
urlpatterns = [
    path('latestsearches/',
         LatestSearchesViewSet.as_view(list_actions),
         name="latestsearches"),

    path('trends/',
         Trends.as_view(list_actions),
         name="trends"),
]
