from django.shortcuts import render
from .models import Tweet
from .serializers import TweetSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound


@api_view(["GET"])
def tweets(request):
    if request.method == "GET":
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
