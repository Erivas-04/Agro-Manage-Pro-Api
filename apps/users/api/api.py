from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from .serializers import UpdateUser, UpdatePasswordSerializer, UserListSerializer
from apps.users.models import User
from ...company.models import UserAsigned
from ...login_logout.authentication_mixins import Authentication


class UserAPI(Authentication, APIView):

    def get(self, request, user_id = None):
        user_asigned = UserAsigned.objects.filter(id = user_id).first()
        user = User.objects.filter(id = user_asigned.user.id).first()
        if not user:
            return Response(data={'message': 'Usuario no encontrado'}, status = status.HTTP_404_NOT_FOUND)

        user_serializer = UserListSerializer(user)

        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id = None):
        user = User.objects.filter(id = user_id).first()

        if user != None:
            user_request = UpdateUser(user, data = request.data)
            if user_request.is_valid():
                user_request.save()
                return Response(data={"message": "Usuario actualizado"}, status= status.HTTP_200_OK)

            return Response(data={"error": user_request.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data={"error": "Usuario no encontrado"}, status= status.HTTP_404_NOT_FOUND)

class PUTPassword(Authentication, generics.UpdateAPIView):
    serializer_class = UpdatePasswordSerializer

    def put(self, request, *args, **kwargs):
        id = self.kwargs.get('user_id')

        user_act = User.objects.filter(id = id).first()
        user_serializer = UpdatePasswordSerializer(user_act, data = request.data)

        if not user_serializer.is_valid():
            return Response(data = {'message': 'Contraseña no valida'},
                            status = status.HTTP_400_BAD_REQUEST)

        user_serializer.save()

        return Response(data={'message': 'Contraseña Actualizada'})