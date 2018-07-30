import datetime
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Searches
from .serializers import (
    SerializerLatestSearches,
    SerializerTrends,
    SerializerSearches,
    SerializerLocations,
)
from .helpers import Twitter


class LatestSearchesViewSet(viewsets.ModelViewSet):
    default_response_headers = {"Access-Control-Allow-Origin": "*"}
    queryset = Searches.objects.all()
    serializer_class = SerializerLatestSearches


class TrendsViewSet(viewsets.ViewSet):
    default_response_headers = {"Access-Control-Allow-Origin": "*"}
    twitter = Twitter()

    def list(self, request):
        serializer = SerializerTrends(self.twitter.trends(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, woeid=None):
        serializer = SerializerTrends(self.twitter.trends(woeid), many=True)
        return Response(serializer.data)


class SearchViewSet(viewsets.ViewSet):
    default_response_headers = {"Access-Control-Allow-Origin": "*"}
    twitter = Twitter()

    def retrieve(self, request, term=None):
        queryset = Searches.objects.filter(search=term)
        serializer = SerializerSearches(data=self.twitter.search(term=term))

        if serializer.is_valid():
            if queryset.count() == 0:
                queryset.create(search=term)
            else:
                queryset[0].modified = datetime.datetime.now()
                queryset[0].save()

            return Response(serializer.data)


class SearchRawQueryViewSet(viewsets.ViewSet):
    default_response_headers = {"Access-Control-Allow-Origin": "*"}
    twitter = Twitter()

    def retrieve(self, request, raw_query=None):
        serializer = SerializerSearches(data=self.twitter.search(raw_query=raw_query))

        if serializer.is_valid():
            return Response(serializer.data)


class LocationsViewSet(viewsets.ViewSet):
    default_response_headers = {"Access-Control-Allow-Origin": "*"}
    twitter = Twitter()

    def list(self, request):
        serializer = SerializerLocations(data=self.twitter.locations(), many=True)

        if serializer.is_valid():
            return Response(serializer.data)
