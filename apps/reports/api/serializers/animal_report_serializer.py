from rest_framework import serializers
from apps.reports.models import AnimalMove, AsigAnimalMove
from apps.cages.models import Cage
from apps.company.models import UserAsigned

class AnimalMoveSerializer(serializers.Serializer):
    id_user = serializers.IntegerField()
    weight = serializers.FloatField(min_value=0)
    age = serializers.FloatField(min_value=0)
    id_cage = serializers.IntegerField()
    type_of_movement = serializers.IntegerField()
    amount = serializers.IntegerField(allow_null=True)

    def create(self, validated_data):
        id_cage = validated_data.pop('id_cage')
        id_user = validated_data.pop('id_user')
        type = validated_data.pop('type_of_movement')
        amount = 1
        try:
            amount = validated_data.pop('amount')
        except:
            amount = 1

        user = UserAsigned.objects.filter(id = id_user).first()
        cage = Cage.objects.filter(id = id_cage).first()

        animal_move = AnimalMove(type = type, user = user, **validated_data)
        animal_move.save()

        AsigAnimalMove.objects.create(animal_move = animal_move, cage = cage)

        if type == 0:
            cage.feed_animal.animal_amount += amount
        else:
            cage.feed_animal.animal_amount -= 1

        cage.feed_animal.save()

        return animal_move