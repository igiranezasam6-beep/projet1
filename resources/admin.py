from django.contrib import admin
from .models import Subject, Level, Exercise, Video

admin.site.register(Subject)
admin.site.register(Level)

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'level', 'teacher', 'created_at')
    list_filter = ('subject', 'level', 'teacher')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'level', 'created_at')
    list_filter = ('subject', 'level')
