from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.company.models import UserAsigned
from apps.reports.models import AsigAnimalMove, AsigAnimalFoodMove
from ..serializers.list_report_serializer import ReportAnimalMoveSerializer, ReportAnimalFoodMoveSerializer
from apps.login_logout.authentication_mixins import Authentication

class ListReport(Authentication, APIView):
    def get(self, request, id_user=None):
        if not id_user:
            return Response(data={'message': 'el id no fue enviado correctamente'}, status=status.HTTP_400_BAD_REQUEST)

        user = UserAsigned.objects.filter(id = id_user).first()

        animal_move = AsigAnimalMove.objects.filter(animal_move__user__company__id = user.company.id)
        animalfood_move = AsigAnimalFoodMove.objects.filter(animalfood_move__user__company__id = user.company.id)

        animal_move_serializer = ReportAnimalMoveSerializer(animal_move, many=True).data
        animalfood_move_serializer = ReportAnimalFoodMoveSerializer(animalfood_move, many=True).data

        report_move = []

        for report in animal_move_serializer:
            if report.animal_move.type == 0:
                report_move.append({
                    "user_name": report.animal_move.user.user.username,
                    "cage_code": report.cage.code,
                    "cage_name": report.cage.name,
                    "movement_type": "Entrada",
                    "animalOrAnimalFood": "ANIMAL",
                    "amount": report.animal_move.amount_animals,
                    "age": report.animal_move.age,
                    "weigth": report.animal_move.weight,
                    "time": report.animal_move.movement_date
                })
            else:
                report_move.append({
                    "user_name": report.animal_move.user.user.username,
                    "cage_code": report.cage.code,
                    "cage_name": report.cage.name,
                    "movement_type": "Salida" if report.animal_move.type == 1 else "Muerte",
                    "animalOrAnimalFood": "ANIMAL",
                    "amount": report.animal_move.amount_animals,
                    "age": report.animal_move.age,
                    "weigth": report.animal_move.weight,
                    "time": report.animal_move.movement_date
                })

        for report in animalfood_move_serializer:
            report_move.append({
                "user_name": report.animalfood_move.user.user.username,
                "cage_code": report.cage.code,
                "cage_name": report.cage.name,
                "movement_type": "Ingreso" if report.animalfood_move.type == 1 else "Uso",
                "animalOrAnimalFood": "CONCENTRADO",
                "amount": report.animalfood_move.amount,
                "age": None,
                "weigth": None,
                "time": report.animalfood_move.date
            })

        return Response(data=report_move, status=status.HTTP_200_OK)