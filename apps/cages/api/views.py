from rest_framework import generics, status
from rest_framework.response import Response

from apps.cages.models import Cage
from apps.cages.api.serializers import CageListSerializer, CageCreateSerializer, AsigAnimal, AsigAnimalFood, CageUpdateSerializer
from apps.company.models import UserAsigned

from apps.login_logout.authentication_mixins import Authentication

class CageListAPIView(Authentication, generics.ListAPIView):
    serializer_class = CageListSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = UserAsigned.objects.filter(id = user_id).first()
        if user:
            return Cage.objects.filter(user__company__id=user.company.id)

        return []

class CageGetAPIView(Authentication, generics.RetrieveAPIView):
    serializer_class = CageListSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(hability = True)



class CageCreateAPIView(Authentication, generics.CreateAPIView):
    serializer_class = CageCreateSerializer

    def post(self, request, *args, **kwargs):
        post_cage = request.data
        post_cage_serializer=CageCreateSerializer(data=post_cage, context=post_cage)
        if post_cage_serializer.is_valid():
            cage_created = post_cage_serializer.save()
            return Response(data={'message': 'Corral creado correctamente',
                                  'id': cage_created.id}, status = status.HTTP_201_CREATED)

class CageUpdateAPIView(Authentication, generics.UpdateAPIView):
    serializer_class = CageUpdateSerializer

    def put(self, request, *args, **kwargs):
        cage_id = self.kwargs.get('cage_id')
        cage_select = Cage.objects.filter(id = cage_id).first()

        if not cage_select:
            return Response(data={'message': 'Corral no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        cage_serializer = CageUpdateSerializer(cage_select, data = request.data)
        if not cage_serializer.is_valid():
            return Response(data={'message': 'Corral invalido'}, status = status.HTTP_400_BAD_REQUEST)

        print(cage_serializer)
        cage_serializer.save()
        return Response(data = {'message': 'Corral actualizado'}, status = status.HTTP_200_OK)

class AsigAnimalUpdateAPIView(Authentication, generics.UpdateAPIView):
    serializer_class = AsigAnimal

    def put(self, request, pk = None ,*args, **kwargs):
        cage_select = Cage.objects.filter(id = pk).first()
        if cage_select:
            asig_animal_serializer = AsigAnimal(cage_select, data=request.data)

            if asig_animal_serializer.is_valid():
                asig_animal_serializer.save()
                return Response(data={'message': 'Animal asignado correctamente'}, status = status.HTTP_200_OK)

            return Response(data={'message': 'Asignacion invalida'}, status = status.HTTP_400_BAD_REQUEST)

        return Response(data={'message': 'Corral no encontrado'}, status = status.HTTP_404_NOT_FOUND)

class AsigAnimalFoodUpdateAPIView(Authentication, generics.UpdateAPIView):
    serializer_class = AsigAnimalFood

    def put(self, request, pk = None, *args, **kwargs):
        cage_select = Cage.objects.filter(id = pk).first()
        if cage_select:
            asig_animal_food_serializer = AsigAnimalFood(cage_select, data = request.data)

            if asig_animal_food_serializer.is_valid():
                asig_animal_food_serializer.save()
                return Response(data={'message': 'Concentrado asignado correctamente'}, status = status.HTTP_200_OK)

            return Response(data={'message': 'Asignacion de concentrado no valido',
                                  'error': asig_animal_food_serializer.errors},
                            status = status.HTTP_400_BAD_REQUEST)

        return Response(data={'message': 'Corral no encontrado'},
                        status = status.HTTP_404_NOT_FOUND)