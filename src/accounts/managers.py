from .base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, user_role, user_password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        username = username
        user = self.model(username=username, user_role=user_role, user_password=user_password)
        user.set_password(user_password)
        user.save(using=self._db)
        return user

    def create_user(self, username, user_role, user_password=None):
        # extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, user_role, user_password)

    def create_superuser(self, username, user_role, user_password):
        # extra_fields.setdefault('is_superuser', True)

        # if extra_fields.get('is_superuser') is not True:
            # raise ValueError('Superuser must have is_superuser=True.')
        user = self.create_user(username=username, user_role=user_role, user_password=user_password)
        return user
        return self._create_user(username, user_role, user_password)
