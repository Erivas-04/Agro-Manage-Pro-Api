from django.urls import path
from apps.users.api.api import UserAPI

urlpatterns = [
    path('', UserAPI.as_view(), name = "user_api"),
    path('<int:pk>', UserAPI.as_view(), name="user_api"),
]