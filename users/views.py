from django.contrib.auth import authenticate, login, logout

from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import User
from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from .serializers import UserSerializer, PrivateUserSerializer


class Users(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = User.objects.all()
        user_serializer = PrivateUserSerializer(users, many=True).data
        return Response(user_serializer)

    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ParseError("비밀번호를 입력해주세요.")
        user_serializer = PrivateUserSerializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            user.set_password(password)
            user.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors, status=400)


class UserDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_queryset(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound("해당 유저가 존재하지 않습니다.")

    def get(self, request, pk):
        user = self.get_queryset(pk)
        user_serializer = PrivateUserSerializer(user).data
        return Response(user_serializer)


class UserTweets(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            raise NotFound("해당 유저가 존재하지 않습니다.")
        try:
            tweets = Tweet.objects.filter(user=user)
        except Tweet.DoesNotExist:
            raise NotFound("해당 유저의 트윗이 존재하지 않습니다.")
        tweet_serializer = TweetSerializer(tweets, many=True)
        return Response(tweet_serializer.data)


class ChangePassword(APIView):

    permission_classes = [IsAuthenticated]

    # 로그인한 유저의 비밀번호 변경
    def put(self, request, pk):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not old_password:
            raise ParseError("기존 비밀번호를 입력해주세요.")
        elif not new_password:
            raise ParseError("새로운 비밀번호를 입력해주세요.")

        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
        else:
            raise ParseError("기존 비밀번호가 일치하지 않습니다.")
        return Response(status=status.HTTP_200_OK)


class Login(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username:
            raise ParseError("아이디를 입력해주세요.")
        elif not password:
            raise ParseError("비밀번호를 입력해주세요.")

        user = authenticate(
            request=request,
            username=username,
            password=password,
        )
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            raise ParseError("아이디 또는 비밀번호가 일치하지 않습니다.")


class Logout(APIView):

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
