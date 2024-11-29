from django.conf import settings
from rest_framework import serializers
from apps.cages.models import Cage
from apps.company.models import UserAsigned
from apps.reports.models import AnimalFoodMove, AsigAnimalFoodMove

class AnimalFoodMoveSerializer(serializers.Serializer):
    id_user = serializers.IntegerField()
    id_cage = serializers.IntegerField()
    amount = serializers.FloatField()
    type = serializers.IntegerField()

    def create(self, validated_data):
        id_user = validated_data.pop('id_user')
        id_cage = validated_data.pop('id_cage')

        user = UserAsigned.objects.filter(id =id_user).first()
        cage = Cage.objects.filter(id = id_cage).first()

        animalfood_move = AnimalFoodMove(user = user, **validated_data)

        if validated_data['type'] == 1:
            cage.feed_animal_food.animal_food_amount += validated_data['amount']
        else:
            cage.feed_animal_food.animal_food_amount -= validated_data['amount']

        animalfood_move.save()

        AsigAnimalFoodMove.objects.create(animalfood_move = animalfood_move, cage = cage)

        cage.feed_animal_food.save()

        return animalfood_move