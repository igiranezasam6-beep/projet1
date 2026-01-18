from django.db import models
from django.conf import settings
from resources.models import Subject, Level
from django.utils.translation import gettext_lazy as _

class Discussion(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Titre'))
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=_('Matière'))
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name=_('Niveau'))
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(verbose_name=_('Contenu'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    discussion = models.ForeignKey(Discussion, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(verbose_name=_('Commentaire'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.discussion}"
