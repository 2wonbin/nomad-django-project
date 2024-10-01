from django.contrib import admin

from .models import Tweet, Like


class WordFilter(admin.SimpleListFilter):
    title = "'Elon Musk' 키워드 포함 여부"

    parameter_name = "is_contain_elon_musk"

    def lookups(self, request, model_admin):
        return (("true", "Yes"),)

    def queryset(self, request, tweets):
        if self.value() == "true":
            return tweets.filter(payload__icontains="Elon Musk")
        return tweets


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

    search_fields = ("payload", "user__username")
    list_filter = (
        WordFilter,
        "created_at",
    )


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
    search_fields = ("user__username",)
    list_filter = ("created_at",)
