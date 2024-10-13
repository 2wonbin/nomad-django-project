from rest_framework.serializers import ModelSerializer

from .models import User


class SimpleUserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            "pk",
            "username",
        ]


class PrivateUserSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "id",
            "groups",
            "user_permissions",
        )


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
