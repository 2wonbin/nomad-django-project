from .models import Tweet
from .serializers import TweetSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound


class Tweets(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        tweet_serializer = TweetSerializer(tweets, many=True)
        return Response({"tweets": tweet_serializer.data})


class TweetDetail(APIView):
    def get(self, request, tweet_id):
        try:
            tweet = Tweet.objects.filter(id=tweet_id).first()
            tweet_serializer = TweetSerializer(tweet)
            return Response(tweet_serializer.data)
        except Tweet.DoesNotExist:
            raise NotFound("해당 트윗이 존재하지 않습니다.")
