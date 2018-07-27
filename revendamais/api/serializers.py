from rest_framework import serializers
from .models import LatestSearches


class SerializerLatestSearches(serializers.ModelSerializer):
    class Meta:
        model = LatestSearches
        fields = '__all__'


class SerializerTrends(serializers.Serializer):
    name = serializers.CharField()
    query = serializers.CharField()
    timestamp = serializers.DateTimeField()
    url = serializers.CharField()
    tweet_volume = serializers.IntegerField()
