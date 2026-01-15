from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    class Role(models.TextChoices):
        STUDENT = "student", "Élève"
        TEACHER = "teacher", "Enseignant"

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)
    is_verified = models.BooleanField(default=False)
    school_level = models.CharField(
        max_length=50,
        blank=True,
        help_text="Ex: 7e, 8e, 9e, 1re, 2e, 3e, Terminale…",
    )

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.user.username} ({self.role})"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_profile(sender, instance: User, created: bool, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        Profile.objects.get_or_create(user=instance)


class Exercise(models.Model):
    subject = models.CharField(max_length=100)
    school_level = models.CharField(max_length=50)
    theme = models.CharField(max_length=120, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    exercise_file = models.FileField(upload_to="exercises/")
    correction_file = models.FileField(upload_to="corrections/", blank=True)
    correction_text = models.TextField(blank=True)
    video_url = models.URLField(blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="exercises"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.subject} · {self.school_level} · {self.title}"


class ExerciseComment(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:  # pragma: no cover
        return f"Comment #{self.pk} on Exercise #{self.exercise_id}"


class ForumTopic(models.Model):
    subject = models.CharField(max_length=100)
    school_level = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=200)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:  # pragma: no cover
        return self.title


class ForumPost(models.Model):
    topic = models.ForeignKey(ForumTopic, on_delete=models.CASCADE, related_name="posts")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self) -> str:  # pragma: no cover
        return f"Post #{self.pk} in Topic #{self.topic_id}"
