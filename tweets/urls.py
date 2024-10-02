from django.urls import path
from . import views

app_name = "tweets"

urlpatterns = [
    path("", views.see_all_tweets, name="tweet_list"),
    path("tweets/<int:tweet_pk>", views.see_one_tweet, name="tweet_detail"),
]
