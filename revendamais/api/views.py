from rest_framework import viewsets
from rest_framework.response import Response
from .models import LatestSearches
from .serializers import SerializerLatestSearches, SerializerTrends
from .helpers import Twitter


class LatestSearchesViewSet(viewsets.ModelViewSet):
    queryset = LatestSearches.objects.all()
    serializer_class = SerializerLatestSearches


class Trends(viewsets.ViewSet):
    twitter = Twitter()
    serializer = SerializerTrends(twitter.trends(), many=True)

    def list(self, request):
        return Response(self.serializer.data)
