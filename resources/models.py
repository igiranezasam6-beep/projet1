from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Matière'))

    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Niveau'))

    def __str__(self):
        return self.name

class Exercise(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Titre'))
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=_('Matière'))
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name=_('Niveau'))
    topic = models.CharField(max_length=200, verbose_name=_('Thème'))
    file = models.FileField(upload_to='exercises/', verbose_name=_('Fichier Exercice'))
    solution_file = models.FileField(upload_to='solutions/', blank=True, null=True, verbose_name=_('Fichier Corrigé'))
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={'role': 'TEACHER'}, verbose_name=_('Enseignant'))
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0, verbose_name=_('Vues'))
    downloads = models.PositiveIntegerField(default=0, verbose_name=_('Téléchargements'))

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Titre'))
    url = models.URLField(verbose_name=_('Lien YouTube'))
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=_('Matière'))
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name=_('Niveau'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
