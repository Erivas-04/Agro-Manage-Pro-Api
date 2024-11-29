from rest_framework import generics, status
from ..serializers.animalfood_report_serializer import AnimalFoodMoveSerializer
from rest_framework.response import Response
from apps.login_logout.authentication_mixins import Authentication

class AnimalFoodMoveCreate(Authentication, generics.CreateAPIView):
    serializer_class = AnimalFoodMoveSerializer

    def post(self, request, id_user = None,*args, **kwargs):
        if not id_user:
            return Response(data={'message': 'es necesario un usuario'}, status=status.HTTP_400_BAD_REQUEST)

        animalfood_move_request = request.data
        animalfood_move_request['id_user'] = id_user

        animalfood_move_serializer = AnimalFoodMoveSerializer(data=animalfood_move_request)

        if not animalfood_move_serializer.is_valid():
            return Response(data={'message': 'datos de concentrado invalido'}, status=status.HTTP_400_BAD_REQUEST)

        animalfood_move_serializer.save()

        return Response(data={'message': 'concentrado registrado correctamente'}, status=status.HTTP_201_CREATED)