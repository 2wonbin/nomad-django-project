from rest_framework.serializers import ModelSerializer

from .models import Tweet
from users.models import User


class SimpleUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            "pk",
            "username",
        ]


class TweetSerializer(ModelSerializer):
    user = SimpleUserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = (
            "pk",
            "user",
            "payload",
            "created_at",
        )
