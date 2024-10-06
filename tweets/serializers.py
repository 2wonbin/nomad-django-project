from rest_framework.serializers import ModelSerializer

from users.serializers import SimpleUserSerializer

from .models import Tweet


class TweetSerializer(ModelSerializer):

    user = SimpleUserSerializer()

    class Meta:
        model = Tweet
        fields = "__all__"
