from django.urls import path
from .views.animal_views import AnimalListAPIView, AnimalCreateAPIView, AnimalUpdateAPIView
from .views.animal_food_views import AnimalFoodListAPIView, AnimalFoodCreateAPIView, AnimalFoodUpdateAPIView

urlpatterns = [
    # animales
    path('list/<int:user_id>', AnimalListAPIView.as_view(), name = 'animal_list'),
    path('create/<int:user_id>', AnimalCreateAPIView.as_view(), name = 'animal_create'),
    path('update/<int:animal_id>', AnimalUpdateAPIView.as_view(), name = 'animal_update'),

    # concentrados
    path('food/list/<int:user_id>', AnimalFoodListAPIView.as_view(), name='animal_food_list'),
    path('food/create/<int:user_id>', AnimalFoodCreateAPIView.as_view(), name='animal_food_create'),
    path('food/update/<int:animal_food_id>', AnimalFoodUpdateAPIView.as_view(), name='animal_food_update'),
]