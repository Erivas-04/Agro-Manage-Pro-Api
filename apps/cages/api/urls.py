from django.urls import path
from .views import CageListAPIView, CageCreateAPIView, AsigAnimalUpdateAPIView, AsigAnimalFoodUpdateAPIView, CageGetAPIView

urlpatterns = [
    path('list/<int:user_id>', CageListAPIView.as_view(), name = 'list_cage'),
    path('create/', CageCreateAPIView.as_view(), name = 'create_cage'),
    path('get/<int:pk>', CageGetAPIView.as_view(), name = 'get_cage'),
    path('asig/<int:pk>/animal', AsigAnimalUpdateAPIView.as_view(), name = 'asig_animal'),
    path('asig/<int:pk>/animal/food', AsigAnimalFoodUpdateAPIView.as_view(), name = 'asig_animal_food'),
]