from apps.animals.api.serializers.animal_food_serializer import AnimalFoodViewSerializer, AnimalFoodCreateUpdateSerializer
from apps.animals.models import AnimalFood
from apps.company.models import UserAsigned
from rest_framework import generics, status
from rest_framework.response import Response
from apps.login_logout.authentication_mixins import Authentication

class AnimalFoodListAPIView(Authentication, generics.ListAPIView):
    serializer_class = AnimalFoodViewSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = UserAsigned.objects.filter(id = user_id).first()
        if user:
            return AnimalFood.objects.filter(user__company__id = user.company.id)

        return []

class AnimalFoodCreateAPIView(Authentication, generics.CreateAPIView):
    serializer_class = AnimalFoodCreateUpdateSerializer

    def post(self, request, user_id = None,*args, **kwargs):
        if not user_id:
            return Response(data={'message': 'Es necesario un id de usuario'}, status = status.HTTP_400_BAD_REQUEST)

        data = request.data
        data['user'] = user_id

        data_serializer = AnimalFoodCreateUpdateSerializer(data = data)

        if not data_serializer.is_valid():
            return Response(data={'message': 'Datos no validos'}, status = status.HTTP_400_BAD_REQUEST)

        data_serializer.save()

        return Response(data={'message': 'Concentrado creado correctamente'}, status = status.HTTP_200_OK)


class AnimalFoodUpdateAPIView(Authentication, generics.UpdateAPIView):
    serializer_class = AnimalFoodCreateUpdateSerializer

    def put(self, request, animal_food_id = None, *args, **kwargs):
        animal_food_select = AnimalFood.objects.filter(id = animal_food_id).first()

        if not animal_food_select:
            return Response(data={'message': 'Concentrado no encontrado'}, status = status.HTTP_404_NOT_FOUND)

        animal_food_request = request.data
        animal_food_request['user'] = 0
        animal_food_serializer = AnimalFoodCreateUpdateSerializer(animal_food_select, data=animal_food_request)

        if not animal_food_serializer.is_valid():
            return Response(data={'message': 'Concentrado no valido'}, status = status.HTTP_400_BAD_REQUEST)

        animal_food_serializer.save()

        return Response(data={'message': 'Concentrado actualizado'}, status =status.HTTP_200_OK)