from django.db import models

from common.models import CommonModel


class Tweet(CommonModel):
    payload = models.TextField(max_length=180)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="tweets")

    def __str__(self):
        return self.payload

    def get_like_count(self):
        return self.like.count()


class Like(CommonModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="like")

    def __str__(self):
        return f"{self.user} likes {self.tweet}"
