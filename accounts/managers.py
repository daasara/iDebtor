from .base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, role):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        username = self.normalize_email(username)
        user = self.model(username=username, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None):
        # extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password)

    def create_superuser(self, username, password, role):
        # extra_fields.setdefault('is_superuser', True)

        # if extra_fields.get('is_superuser') is not True:
            # raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, role)
