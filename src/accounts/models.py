from __future__ import unicode_literals

from django.db import models
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager
from .base_user import AbstractBaseUser


class User(AbstractBaseUser):
    # email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=30, unique=True, blank=False)
    # first_name = models.CharField(_('first name'), max_length=30, blank=True)
    # last_name = models.CharField(_('last name'), max_length=30, blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    ROLEA = 'RoleA'
    ROLEB = 'RoleB'

    USER_ROLES = ((ROLEA, 'RoleA'),
                  (ROLEB, 'RoleB'))

    user_role = models.CharField(max_length=20, choices=USER_ROLES, default=ROLEA)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['user_role']

    class Meta:
        db_table = 'tbl_users'
        verbose_name = _('user')
        verbose_name_plural = _('users')
