from django.urls import path
from .views import home

app_name = 'api'
urlpatterns = [
    path('teste/', view=home, name='home')
]
