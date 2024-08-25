from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from accounts.tasks import send_email
from config.celery import app


class User(AbstractUser):
    email = models.EmailField(_("email address"), null=False, blank=False, unique=True)
    special_user = models.DateTimeField(default=timezone.now)
    task_id = models.CharField(null=True, blank=True, max_length=30)

    def is_special_user(self):
        return timezone.now() < self.special_user

    is_special_user.boolean = True
    is_special_user.short_description = "Special User"
