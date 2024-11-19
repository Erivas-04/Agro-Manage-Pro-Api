from rest_framework.response import Response
from rest_framework import status
from .authentication import ExpiringTokenAuthentication
from rest_framework.authentication import get_authorization_header
from rest_framework.renderers import JSONRenderer

class Authentication(object):

    def get_user(self, request):
        token, user, message, is_expired = None, None, None, None
        token = get_authorization_header(request).split()
        if token:
            try:
                token = token[1].decode()
            except:
                return (message, is_expired)

            token_expired = ExpiringTokenAuthentication()

            user, token, message, is_expired = token_expired.authenticate_credentials(token)

            if message:
                return (message, is_expired)
            return (user, is_expired)

        return (message, is_expired)


    def dispatch(self, request, *args, **kwargs):
        user, is_expired = self.get_user(request)
        response = None
        if not user:
            response = Response({'message': 'no se han enviado credenciales'}, status=status.HTTP_400_BAD_REQUEST)
        elif type(user) == str:
            if is_expired:
                response = Response({'message': user}, status = status.HTTP_408_REQUEST_TIMEOUT)
            else:
                response = Response({'message': user}, status = status.HTTP_400_BAD_REQUEST)
        else:
            return super().dispatch(request, *args, **kwargs)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response