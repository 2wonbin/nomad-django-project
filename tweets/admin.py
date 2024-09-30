from django.contrib import admin

from .models import Tweet, Like


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Tweet",
            {
                "fields": (
                    "payload",
                    "user",
                ),
                "classes": ("wide",),
            },
        ),
        (
            "Dates",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )
    readonly_fields = ("created_at", "updated_at")
    list_display = ("payload", "user", "get_like_count")


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Like",
            {
                "fields": (
                    "user",
                    "tweet",
                ),
                "classes": ("wide",),
            },
        ),
        (
            "Dates",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )
    readonly_fields = ("created_at", "updated_at")
    list_display = ("user", "tweet")
