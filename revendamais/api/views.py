from rest_framework import viewsets
from rest_framework.response import Response
from .models import LatestSearches
from .serializers import (SerializerLatestSearches,
                          SerializerTrends,
                          SerializerSearches,
                          SerializerLocations)
from .helpers import Twitter


class LatestSearchesViewSet(viewsets.ModelViewSet):
    default_response_headers = {'Access-Control-Allow-Origin': '*'}
    queryset = LatestSearches.objects.all()
    serializer_class = SerializerLatestSearches


class TrendsViewSet(viewsets.ViewSet):
    default_response_headers = {'Access-Control-Allow-Origin': '*'}
    twitter = Twitter()

    def list(self, request, woeid=None):
        serializer = SerializerTrends(self.twitter.trends(woeid), many=True)
        return Response(serializer.data)


class SearchViewSet(viewsets.ViewSet):
    default_response_headers = {'Access-Control-Allow-Origin': '*'}
    twitter = Twitter()

    def list(self, request, search):
        serializer = SerializerSearches(data=self.twitter.search(search))

        if serializer.is_valid():
            return Response(serializer.data)


class LocationsViewSet(viewsets.ViewSet):
    default_response_headers = {'Access-Control-Allow-Origin': '*'}
    twitter = Twitter()

    def list(self, request):
        serializer = SerializerLocations(data=self.twitter.locations(),
                                         many=True)

        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
