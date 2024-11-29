from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from apps.company.models import UserAsigned


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context= {'request': request})
        if not login_serializer.is_valid():
            return Response({'message': 'el usuario enviado es invalido'}, status=status.HTTP_400_BAD_REQUEST)

        user = login_serializer.validated_data['user']
        if not user.is_active:
            return Response({'message': 'este usuario no está activo'}, status=status.HTTP_401_UNAUTHORIZED)

        user_asigned = UserAsigned.objects.filter(user__id = user.id).first()

        token,created = Token.objects.get_or_create(user = user)

        return Response({
            'token': token.key,
            'asig': user_asigned.id
        }, status = status.HTTP_201_CREATED)

# class Logout(APIView):
#     def post(self,request, *args, **kwargs):
#         token = request.GET.get('token')
#