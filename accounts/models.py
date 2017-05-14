from django.db import models
from django_custom_user_migration.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = 'tbl_users'
        managed = True
