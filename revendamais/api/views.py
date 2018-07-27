from rest_framework import viewsets
from .models import LatestSearches
from .serializers import SerializerLatestSearches


class LatestSearchesViewSet(viewsets.ModelViewSet):
    queryset = LatestSearches.objects.all()
    serializer_class = SerializerLatestSearches
