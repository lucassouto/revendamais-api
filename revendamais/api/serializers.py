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


class SerializerUser(serializers.Serializer):
    id_str = serializers.CharField()
    name = serializers.CharField()
    screen_name = serializers.CharField()
    description = serializers.CharField(allow_blank=True)
    url = serializers.CharField(allow_null=True)
    followers_count = serializers.IntegerField()
    friends_count = serializers.IntegerField()
    listed_count = serializers.IntegerField()
    created_at = serializers.CharField()
    favourites_count = serializers.IntegerField()
    statuses_count = serializers.CharField()
    lang = serializers.CharField()
    profile_background_image_url = serializers.CharField(allow_null=True)
    profile_background_image_url_https = serializers.CharField(allow_null=True)
    profile_image_url = serializers.CharField()
    profile_image_url_https = serializers.CharField()
    profile_banner_url = serializers.CharField()
    following = serializers.BooleanField()


class SerializerEntities(serializers.Serializer):
    hashtags = serializers.ListField(allow_null=True)
    symbols = serializers.ListField(allow_null=True)
    user_mentions = serializers.ListField(allow_null=True)
    urls = serializers.JSONField(allow_null=True)


class SerializerTweets(serializers.Serializer):
    created_at = serializers.CharField()
    id_str = serializers.CharField()
    text = serializers.CharField()
    source = serializers.CharField()
    in_reply_to_screen_name = serializers.CharField()
    in_reply_to_status_id = serializers.CharField()
    in_reply_to_user_id = serializers.CharField()
    retweet_count = serializers.IntegerField()
    favorite_count = serializers.IntegerField()
    lang = serializers.CharField()
    user = SerializerUser()
    entities = SerializerEntities()


class SerializerSearchMetaData(serializers.Serializer):
    completed_in = serializers.DurationField()
    max_id_str = serializers.CharField()
    next_results = serializers.CharField()
    query = serializers.CharField()
    count = serializers.IntegerField()
    since_id_str = serializers.CharField()


class SerializerSearches(serializers.Serializer):
    statuses = SerializerTweets(many=True)
    search_metadata = SerializerSearchMetaData()


class SerializerLocations(serializers.Serializer):
    name = serializers.CharField()
    woeid = serializers.IntegerField()
