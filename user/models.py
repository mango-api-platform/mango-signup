from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    left = models.DateTimeField(null=True, blank=True, db_index=True, help_text='탈퇴일시', verbose_name='탈퇴일시')
