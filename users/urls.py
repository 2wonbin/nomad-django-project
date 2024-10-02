from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("/<int:user_id>/tweets", views.user_tweets, name="user_tweets"),
]
