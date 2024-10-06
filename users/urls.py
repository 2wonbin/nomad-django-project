from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path(
        "<int:user_id>/tweets",
        views.UserTweets.as_view(),
        name="user_tweets",
    ),
]
