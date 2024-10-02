from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()
    created_at = serializers.DateTimeField()
