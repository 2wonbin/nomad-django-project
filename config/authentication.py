from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import User


class UsernameAuthentication(BaseAuthentication):

    def authenticate(self, request):
        username = request.headers.get("X-USERNAME")

        if not username:
            return None
        try:
            user = User.objects.get(username=username)
            return (user, None)
        except User.DoesNotExist:
            raise AuthenticationFailed("f{username} 유저가 존재하지 않습니다.")
        except Exception as e:
            raise AuthenticationFailed("알 수 없는 오류가 발생했습니다.") from e
