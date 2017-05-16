from django.contrib.auth.hashers import check_password
from .models import User


class MyAuth(object):

    def authenticate(self, username="", password=""):
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                return user
            else:
                return None
        except User.DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None

    # Required for your backend to work properly - unchanged in most scenarios
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def user_can_authenticate(self, user):
        True
