from django.urls import path
from .views.animal_report_view import AnimalMoveCreate
from .views.animalfood_report_view import AnimalFoodMoveCreate
from .views.list_report_view import ListReport

animal_url = [
    path('animal/<int:id_user>', AnimalMoveCreate.as_view(), name = 'animal_report')
]

animalfood_url = [
    path('animalfood/<int:id_user>', AnimalFoodMoveCreate.as_view(), name = 'animalfood_report')
]

list_url =[
    path('list/<int:id_user>', ListReport.as_view(), name = 'reports_list')
]

urlpatterns = animal_url + animalfood_url + list_url