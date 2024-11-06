from rest_framework import serializers

from apps.animals.models import Animal, AnimalFood
from apps.cages.models import Cage, FeedAnimal, FeedAnimalFood
from django.core.validators import MinLengthValidator

from apps.company.models import UserAsigned


class CageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cage
        fields = '__all__'

    def to_representation(self, instance):
        representation = {
            'id': instance.id,
            'user': instance.user.user.name,
            'code': instance.code,
            'name': instance.name,
            'hability': instance.hability,
            'observations': instance.observations,
            'feed_animal': instance.feed_animal.animal_amount,
            'feed_animal_food': instance.feed_animal_food.animal_food_amount,
        }
        try:
            representation['animal'] = instance.animal.animal_name
        except:
            representation['animal'] = "No hay animal asignado"

        try:
            representation['animal_food'] = instance.animal_food.animal_food_name
        except:
            representation['animal_food'] = "No hay concentrado asignado"

        return representation

class CageCreateSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    code = serializers.CharField(max_length=8,
                                 min_length=1)
    name = serializers.CharField(max_length=30,
                                 min_length=8)
    hability = serializers.BooleanField()
    observations = serializers.CharField(max_length=100,
                                         allow_blank=True)

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        feed_animal = FeedAnimal.objects.create(animal_amount = 0)
        feed_animal_food = FeedAnimalFood.objects.create(animal_food_amount = 0)
        user = UserAsigned.objects.filter(id = user_data).first()

        cage = Cage.objects.create(feed_animal = feed_animal, feed_animal_food = feed_animal_food, user = user, **validated_data)
        return cage

class AsigAnimal(serializers.Serializer):
    animal = serializers.IntegerField()
    animal_amount = serializers.IntegerField()

    def update(self, instance, validated_data):

        animal = Animal.objects.filter(id = validated_data['animal']).first()
        instance.animal = animal
        instance.save()

        animal_amount = FeedAnimal.objects.filter(id = instance.feed_animal.id).first()
        animal_amount.animal_amount = validated_data.get('animal_amount', animal_amount.animal_amount)
        animal_amount.save()

        return validated_data

class AsigAnimalFood(serializers.Serializer):
    animal_food = serializers.IntegerField()
    animal_food_amount = serializers.FloatField()

    def update(self, instance, validated_data):

        animal_food = AnimalFood.objects.filter(id = validated_data['animal_food']).first()
        instance.animal_food = animal_food
        instance.save()

        animal_food_amount_request = FeedAnimalFood.objects.filter(id = instance.feed_animal_food.id).first()
        animal_food_amount_request.animal_food_amount = validated_data.get('animal_food_amount', animal_food_amount_request.animal_food_amount)
        animal_food_amount_request.save()

        return validated_data