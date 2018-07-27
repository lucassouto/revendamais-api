from rest_framework import serializers
from .models import LatestSearches


class SerializerLatestSearches(serializers.ModelSerializer):
    class Meta:
        model = LatestSearches
        fields = '__all__'
