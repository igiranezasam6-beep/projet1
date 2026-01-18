from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = 'STUDENT', _('Élève')
        TEACHER = 'TEACHER', _('Enseignant')
        ADMIN = 'ADMIN', _('Administrateur')

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT,
        verbose_name=_('Rôle')
    )
    is_verified = models.BooleanField(
        default=False,
        verbose_name=_('Compte vérifié'),
        help_text=_('Uniquement pour les enseignants.')
    )

    def is_teacher(self):
        return self.role == self.Role.TEACHER

    def is_student(self):
        return self.role == self.Role.STUDENT
