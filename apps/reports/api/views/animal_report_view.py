from rest_framework.response import Response
from ..serializers.animal_report_serializer import AnimalMoveSerializer
from rest_framework import generics, status
from apps.login_logout.authentication_mixins import Authentication

class AnimalMoveCreate(Authentication, generics.CreateAPIView):
    serializer_class = AnimalMoveSerializer

    def post(self, request, id_user = None ,*args, **kwargs):
        if not id_user:
            return Response(data={'message': 'usuario no enviado'}, status=status.HTTP_400_BAD_REQUEST)

        animalmove_request = request.data
        animalmove_request['id_user'] = id_user

        animalmove_serializer = AnimalMoveSerializer(data=animalmove_request)

        if not animalmove_serializer.is_valid():
            return Response(data={'message': 'Datos de reporte invalido', 'error': animalmove_serializer.errors},
                            status = status.HTTP_400_BAD_REQUEST)

        animalmove_serializer.save()

        return Response(data={'message': 'Animal registrado correctamente'},
                        status = status.HTTP_201_CREATED)
