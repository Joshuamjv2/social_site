from django.contrib.auth.models import User

# Here we are creating an authentication backend that logs in a user with their email address.
class EmailAuthBackend(object):
    """
    Authenticate using e-mail address
    """
    def authenticate(self, request, username=None, password=None):
        try:
            # we provide an email address instead of a real username since django logs in with a username by default. below we check if the provided username (supposedly email) matches with any of the emails in the database and check if the passoword of that email corresponds.
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None