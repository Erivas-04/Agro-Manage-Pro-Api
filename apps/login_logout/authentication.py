from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

class ExpiringTokenAuthentication(TokenAuthentication):

    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        return timedelta(seconds = settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapsed

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)

    def token_expire_handler(self, token):
        is_expired = self.is_token_expired(token)

        return is_expired

    def authenticate_credentials(self, key):
        user, token, message = None, None, None
        try:
            token = self.get_model().objects.select_related('user').get(key = key)
            user = token.user
        except self.get_model().DoesNotExist:
            message = 'Token invalido'
            return (user, token, message, False)

        if not token.user.is_active:
            message = 'Usuario no activo'

        is_expired = self.token_expire_handler(token)

        if is_expired:
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user=user)
            message = 'Token expirado'

        user = token.user

        return (user, token, message, is_expired)