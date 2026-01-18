from django.contrib import admin
from .models import Discussion, Comment

@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'level', 'author', 'created_at')

admin.site.register(Comment)
