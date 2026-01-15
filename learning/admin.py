from django.contrib import admin

from .models import Exercise, ExerciseComment, ForumPost, ForumTopic, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "is_verified", "school_level")
    list_filter = ("role", "is_verified")
    search_fields = ("user__username", "user__email")


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "school_level", "theme", "created_by", "created_at", "view_count")
    list_filter = ("subject", "school_level")
    search_fields = ("title", "subject", "theme")


@admin.register(ExerciseComment)
class ExerciseCommentAdmin(admin.ModelAdmin):
    list_display = ("exercise", "author", "created_at")
    search_fields = ("exercise__title", "author__username", "content")


@admin.register(ForumTopic)
class ForumTopicAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "school_level", "created_by", "created_at")
    list_filter = ("subject", "school_level")
    search_fields = ("title", "subject")


@admin.register(ForumPost)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ("topic", "author", "created_at")
    search_fields = ("topic__title", "author__username", "content")
