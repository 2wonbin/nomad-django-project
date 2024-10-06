from django.urls import path
from . import views

app_name = "tweets"

urlpatterns = [
    path("", views.Tweets.as_view(), name="all_tweet_list"),
    path("<int:tweet_id>", views.TweetDetail.as_view(), name="tweet_detail"),
]
