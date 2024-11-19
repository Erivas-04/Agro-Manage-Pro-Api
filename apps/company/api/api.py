from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from .serializer import CompanySerializer, UserAsignedSerializer
from apps.company.models import Company, UserAsigned
from apps.users.api.serializers import CreateUser
from apps.login_logout.authentication_mixins import Authentication

class CompanyApiView(Authentication, APIView):
    def get(self, request, pk = None):
        if pk != None:
            user = UserAsigned.objects.filter(id = pk).first()
            if user == None:
                return Response(data={'message': 'Empresa no encontrada'}, status = status.HTTP_404_NOT_FOUND)

            company = Company.objects.filter(id = user.company.id).first()

            company_serializer = CompanySerializer(company)
            return Response(data=company_serializer.data, status=status.HTTP_200_OK)

        return Response(data={'message': 'No es posible buscar una empresa sin id'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk = None):
        company_select = Company.objects.filter(id = pk).first()

        if company_select:
            company_act = CompanySerializer(company_select, data = request.data)

            if company_act.is_valid():
                company_act.save()
                return Response(data={'message': 'Empresa Actualizada'},
                                status=status.HTTP_200_OK)

            return Response(data={'message': 'la empresa no es valida', 'error': company_act.errors},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response(data={'message': 'Empresa no encontrada'},
                        status= status.HTTP_404_NOT_FOUND)

class CompanyCreateView(Authentication, APIView):
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

class UserAsignedAPI(Authentication, APIView):
    def get(self, request, pk = None):
        if pk != None:
            user = UserAsigned.objects.filter(id = pk).first()

            if user:
                users_list = UserAsigned.objects.filter(company = user.company.id)
                user_select_serializer = UserAsignedSerializer(users_list, many=True)
                return Response(data=user_select_serializer.data,
                                status=status.HTTP_200_OK)

            return Response(data={'message': 'Usuario no encontrado'},
                            status=status.HTTP_404_NOT_FOUND)

        return Response(data={'message': 'Es obligatorio un id'})

class UserAsignedCreateAPIView(Authentication, generics.CreateAPIView):
    serializer_class = UserAsignedSerializer

    def post(self, request,user_id = None, *args, **kwargs):
        user_serializer = CreateUser(data = request.data)
        if not user_serializer.is_valid():
            return Response(data={'message': 'usuario no valido', 'error': user_serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

        creator_user = UserAsigned.objects.filter(id = user_id).first()
        company = Company.objects.filter(id = creator_user.company.id).first()

        user_saved = user_serializer.save()
        asigned = {
            'user': user_saved.id,
            'company': company.id
        }

        asigned_serializer = UserAsignedSerializer(data = asigned)
        if not asigned_serializer.is_valid():
            return Response(data = {'message': 'Algo fue invalido en la empresa'}, status = status.HTTP_400_BAD_REQUEST)

        asigned_serializer.save()

        return Response(data={'message': 'usuario creado correctamente'}, status = status.HTTP_201_CREATED)