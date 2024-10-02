from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import User
from tweets.models import Tweet
from tweets.serializers import TweetSerializer


@api_view(["GET"])
def user_tweets(request, user_id):
    if request.method == "GET":
        # user_id로 user 먼저 조회
        try:
            user = User.objects.filter(id=user_id).first()
        except User.DoesNotExist:
            raise NotFound("해당 사용자는 존재하지 않습니다.")

        tweets = Tweet.objects.filter(user=user)
        tweet_serializer = TweetSerializer(tweets, many=True)
        return Response({"tweets": tweet_serializer.data})
