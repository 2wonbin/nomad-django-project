from .models import Tweet
from .serializers import TweetSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import status

from django.db import transaction


class Tweets(APIView):
    def get(self, request):
        tweets = Tweet.objects.all()
        tweet_serializer = TweetSerializer(tweets, many=True)
        return Response(tweet_serializer.data)

    def post(self, request):
        tweet_serializer = TweetSerializer(data=request.data, context={"request": request})
        if tweet_serializer.is_valid():
            try:
                with transaction.atomic():
                    tweet = tweet_serializer.save(user=request.user)
                return Response(
                    TweetSerializer(tweet, context={"request": request}).data, status=status.HTTP_201_CREATED
                )
            except Exception as e:
                return Response({"error": f"잘못된 요청입니다. {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(tweet_serializer.errors, status=400)


class TweetDetail(APIView):

    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound("해당 트윗이 존재하지 않습니다.")

    def get(self, request, pk):
        try:
            tweet = self.get_object(pk)
            tweet_serializer = TweetSerializer(tweet, context={"request": request})
            return Response(tweet_serializer.data)
        except Tweet.DoesNotExist:
            raise NotFound("해당 트윗이 존재하지 않습니다.")

    def put(self, request, pk):
        tweet = self.get_object(pk)
        tweet_serializer = TweetSerializer(
            tweet,
            data=request.data,
            partial=True,
            context={"request": request},
        )
        if tweet_serializer.is_valid():
            tweet = tweet_serializer.save()
            return Response(TweetSerializer(tweet, context={"request": request}).data)
        return Response(tweet_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tweet = self.get_object(pk)
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
