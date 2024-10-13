from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("", views.Users.as_view(), name="users"),
    path("login", views.Login.as_view(), name="user_login"),
    path("logout", views.Logout.as_view(), name="user_logout"),
    path("<int:pk>", views.UserDetail.as_view(), name="user_detail"),
    path("<int:pk>/tweets", views.UserTweets.as_view(), name="user_tweets"),
    path("<int:pk>/password", views.ChangePassword.as_view(), name="user_password"),
]
