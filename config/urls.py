from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from revendamais.api.urls import router


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('api/v1/',
         include((router.urls, 'api'), namespace='api:api')),
]
