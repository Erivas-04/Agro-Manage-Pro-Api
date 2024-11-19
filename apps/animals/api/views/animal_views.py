from apps.animals.api.serializers.animal_serializer import AnimalViewSerializer, AnimalCreateUpdateSerializer
from apps.animals.models import Animal
from apps.company.models import UserAsigned
from rest_framework import generics, status
from rest_framework.response import Response
from apps.login_logout.authentication_mixins import Authentication

class AnimalListAPIView(Authentication,generics.ListAPIView):
    serializer_class = AnimalViewSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = UserAsigned.objects.filter(id = user_id).first()
        if user:
            return Animal.objects.filter(user__company__id=user.company.id)

        return []

class AnimalCreateAPIView(Authentication, generics.CreateAPIView):
    serializer_class = AnimalCreateUpdateSerializer

    def post(self, request, user_id = None, *args, **kwargs):
        if not user_id:
            return Response(data={'message': 'Es necesario un usuario'}, status = status.HTTP_400_BAD_REQUEST)

        animal_request = request.data
        animal_request['user'] = user_id

        animal_request_serializer = AnimalCreateUpdateSerializer(data = animal_request)

        if not animal_request_serializer.is_valid():
            return Response(data={'message': 'Datos del animal invalidos'},
                            status = status.HTTP_400_BAD_REQUEST)

        animal_request_serializer.save()

        return Response(data={'message': 'Animal creado correctamente'}, status = status.HTTP_201_CREATED)

class AnimalUpdateAPIView(Authentication, generics.UpdateAPIView):
    serializer_class = AnimalCreateUpdateSerializer

    def put(self, request, animal_id = None,*args, **kwargs):
        if not animal_id:
            return Response(data={'message': 'Es necesario un id para la busqueda'}, status = status.HTTP_400_BAD_REQUEST)
        animal_select = Animal.objects.filter(id = animal_id).first()

        if not animal_select:
            return Response(data={'message': 'Animal no encontrado'}, status = status.HTTP_404_NOT_FOUND)

        animal_data_request = request.data
        animal_data_request['user'] = 0

        animal_serializer = AnimalCreateUpdateSerializer(animal_select, animal_data_request)

        if not animal_serializer.is_valid():
            return Response(data={'message': 'Datos de animal invalidos',
                                  'error': animal_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

        animal_serializer.save()
        return Response(data={'meesage': 'Animal actualizado correctamente'}, status = status.HTTP_200_OK)