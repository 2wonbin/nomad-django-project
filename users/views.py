from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework import status

from .models import User
from tweets.models import Tweet
from tweets.serializers import TweetSerializer


class UserTweets(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound("해당 유저가 존재하지 않습니다.")
        try:
            tweets = Tweet.objects.filter(user=user)
        except Tweet.DoesNotExist:
            raise NotFound("해당 유저의 트윗이 존재하지 않습니다.")
        tweet_serializer = TweetSerializer(tweets, many=True)
        return Response(tweet_serializer.data)
