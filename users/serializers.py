from rest_framework.serializers import ModelSerializer

from .models import User


class SimpleUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",
        ]


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
