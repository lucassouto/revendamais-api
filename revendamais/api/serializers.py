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
    created_at = serializers.DateTimeField()
    default_profile = serializers.BooleanField()
    description = serializers.CharField()
    favourites_count = serializers.IntegerField()
    followers_count = serializers.IntegerField()
    following = serializers.BooleanField()
    friends_count = serializers.IntegerField()
    id = serializers.CharField()
    id_str = serializers.CharField()
    lang = serializers.CharField()
    name = serializers.CharField()
    profile_background_color = serializers.CharField()
    profile_background_image_url = serializers.CharField()
    profile_background_image_url_https = serializers.CharField()
    profile_banner_url = serializers.CharField()
    profile_image_url = serializers.CharField()
    profile_image_url_https = serializers.CharField()
    profile_link_color = serializers.CharField()
    profile_sidebar_border_color = serializers.CharField()
    profile_sidebar_fill_color = serializers.CharField()
    profile_text_color = serializers.CharField()
    profile_use_background_image = serializers.CharField()
    screen_name = serializers.CharField()
    statuses_count = serializers.CharField()


class SerializerSearches(serializers.Serializer):
    created_at = serializers.DateTimeField()
    hashtags = serializers.CharField()
    id = serializers.CharField()
    id_str = serializers.CharField()
    in_reply_to_screen_name = serializers.CharField()
    in_reply_to_status_id = serializers.CharField()
    in_reply_to_user_id = serializers.CharField()
    lang = serializers.CharField()
    source = serializers.CharField()
    text = serializers.CharField()
    urls = serializers.CharField()
    user = SerializerUser()
