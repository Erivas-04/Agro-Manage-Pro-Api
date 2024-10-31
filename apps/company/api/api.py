from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import CompanySerializer, UserAsignedSerializer
from apps.company.models import Company, UserAsigned
from apps.users.models import User

class CompanyApiView(APIView):
    def get(self, request, pk = None):
        if pk != None:
            company = Company.objects.filter(id = pk).first()
            if company == None:
                return Response(data={'message': 'Empresa no encontrada'}, status = status.HTTP_404_NOT_FOUND)

            company_serializer = CompanySerializer(company)
            return Response(data={'company': company_serializer.data}, status=status.HTTP_200_OK)

        return Response(data={'message': 'No es posible buscar una empresa sin id'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk = None):
        company_select = Company.objects.filter(id = pk).first()

        if company_select != None:
            company_act = CompanySerializer(company_select, data = request.data)

            if company_act.is_valid():
                company_act.save()
                return Response(data={'message': 'Empresa Actualizada'},
                                status=status.HTTP_200_OK)

            return Response(data={'message': 'la empresa no es valida', 'error': company_act.errors},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response(data={'message': 'Empresa no encontrada'},
                        status= status.HTTP_404_NOT_FOUND)

class CompanyCreateView(APIView):
    def post(self, request):
        company_request = CompanySerializer(data = request.data, context=request.data)
        if company_request.is_valid():
            company_request.save()
            return Response(data={'message': 'Empresa creada correctamente'},
                            status=status.HTTP_201_CREATED)

        return Response(data={'message': 'No se ha podido crear la empresa',
                              'error': company_request.errors
                              },
                        status = status.HTTP_400_BAD_REQUEST)

class UserAsignedAPI(APIView):
    def get(self, request, pk = None):
        if pk != None:
            user_select = UserAsigned.objects.filter(company = pk)

            if user_select:
                user_select_serializer = UserAsignedSerializer(user_select, many=True)
                return Response(data={'User': user_select_serializer.data},
                                status=status.HTTP_200_OK)

            return Response(data={'message': 'Usuario no encontrado'},
                            status=status.HTTP_404_NOT_FOUND)

        all_users = UserAsigned.objects.all()
        all_users_serializer = UserAsignedSerializer(all_users, many=True)
        return Response(data={'users': all_users_serializer.data}, status=status.HTTP_200_OK)


    def post(self, request):
        user = User.objects.create_user(request.data['user']['username'],
                                 None,
                                 request.data['user']['name'],
                                 request.data['user']['last_name'],
                                 None,
                                 tel = request.data['user']['tel'],
                                 observations = request.data['user']['observations'],
                                 change_password = request.data['user']['change_password'],
                                 change_password_next_session = request.data['user']['change_password_next_session'],
                                 is_active = request.data['user']['is_active'])


        request.data['user'] = user.id

        user_request = UserAsignedSerializer(data = request.data, context=request.data)

        if user_request.is_valid():
            user_request.save()
            return Response(data={'message': 'Usuario creado correctamente'},
                            status = status.HTTP_201_CREATED)

        return Response(data={'message': 'Usuario no valido',
                              'error': user_request.errors},
                        status=status.HTTP_400_BAD_REQUEST)