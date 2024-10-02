from rest_framework import serializers


class TweetSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    payload = serializers.CharField()
    user = serializers.CharField()
    created_at = serializers.DateTimeField()
