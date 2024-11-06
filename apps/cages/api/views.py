from rest_framework import generics, status
from rest_framework.response import Response

from apps.cages.models import Cage
from apps.cages.api.serializers import CageListSerializer, CageCreateSerializer, AsigAnimal, AsigAnimalFood


class CageListAPIView(generics.ListAPIView):
    serializer_class = CageListSerializer

    def get_queryset(self):
        company_id = self.kwargs.get('company_id')
        return Cage.objects.filter(user__company__id = company_id)


class CageCreateAPIView(generics.CreateAPIView):
    serializer_class = CageCreateSerializer

    def post(self, request, *args, **kwargs):
        post_cage = request.data
        post_cage_serializer=CageCreateSerializer(data=post_cage, context=post_cage)
        if post_cage_serializer.is_valid():
            post_cage_serializer.save()
            return Response(data={'message': 'Corral creado correctamente'}, status = status.HTTP_201_CREATED)

class AsigAnimalUpdateAPIView(generics.UpdateAPIView):
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

class AsigAnimalFoodUpdateAPIView(generics.UpdateAPIView):
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