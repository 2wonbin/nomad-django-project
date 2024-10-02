from django.urls import path
from . import views

app_name = "tweets"

urlpatterns = [
    path("", views.tweets, name="all_tweet_list"),
]
