from django.urls import path
from .views import LatestSearchesViewSet


list_actions = {
    'get': 'list',
    'post': 'create'
}

app_name = 'api'
urlpatterns = [
    path('latestsearches/',
         LatestSearchesViewSet.as_view(list_actions),
         name="latestsearches"),
]
