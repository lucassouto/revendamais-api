from rest_framework.routers import DefaultRouter
from .views import LatestSearchesViewSet


app_name = 'api'
router = DefaultRouter()
router.register('latestsearches',
                LatestSearchesViewSet,
                base_name='latestsearches')
