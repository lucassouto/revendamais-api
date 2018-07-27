from rest_framework import viewsets
from rest_framework.response import Response
from .models import LatestSearches
from .serializers import (SerializerLatestSearches,
                          SerializerTrends,
                          SerializerSearches)
from .helpers import Twitter


class LatestSearchesViewSet(viewsets.ModelViewSet):
    queryset = LatestSearches.objects.all()
    serializer_class = SerializerLatestSearches


class TrendsViewSet(viewsets.ViewSet):
    twitter = Twitter()

    def list(self, request):
        serializer = SerializerTrends(self.twitter.trends(), many=True)
        return Response(serializer.data)


class SearchViewSet(viewsets.ViewSet):
    twitter = Twitter()

    def list(self, request, search):
        serializer = SerializerSearches(self.twitter.search(search),
                                        many=True)

        return Response(serializer.data)
