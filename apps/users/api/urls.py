from django.urls import path
from apps.users.api.api import UserAPI, PUTPassword

urlpatterns = [
    path('', UserAPI.as_view(), name = "user_api"),
    path('<int:pk>', UserAPI.as_view(), name="user_api"),
    path('<int:user_id>/update/', UserAPI.as_view(), name = 'update_user'),
    path('<int:user_id>/update/pass', PUTPassword.as_view(), name='update_user_password'),
]