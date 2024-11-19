from .api import CompanyApiView, CompanyCreateView, UserAsignedAPI, UserAsignedCreateAPIView
from django.urls import path


urlpatterns = [
    path('create/', CompanyCreateView.as_view(), name = 'company_api'),
    path('<int:pk>', CompanyApiView.as_view(), name = 'company_api'),
    # urls de usuarios
    path('user/create/<int:user_id>', UserAsignedCreateAPIView.as_view(), name= 'user_company_create'),
    path('user/<int:pk>', UserAsignedAPI.as_view(), name = 'user_company_api'),
]
