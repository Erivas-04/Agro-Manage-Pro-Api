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
        try:
            animal_asigned = {
                'animalId': instance.animal.id,
                'animalName': instance.animal.animal_name,
                'animalAmount': instance.feed_animal.animal_amount
            }
        except:
            animal_asigned = {
                'animalId': 0,
                'animalName': "Animal no asignado",
                'animalAmount': instance.feed_animal.animal_amount
            }

        try:
            animal_food_asigned = {
                'concentrateId': instance.animal_food.id,
                'concentrateName': instance.animal_food.animal_food_name,
                'concentrateAmount': instance.feed_animal_food.animal_food_amount
            }
        except:
            animal_food_asigned = {
                'concentrateId': 0,
                'concentrateName': "Concentrado no asignado",
                'concentrateAmount': instance.feed_animal_food.animal_food_amount
            }

        representation = {
            'id': instance.id,
            'code': instance.code,
            'name': instance.name,
            'active': instance.hability,
            'observations': instance.observations,
            'animalAsigned': animal_asigned,
            'concentrateAsigned': animal_food_asigned,
        }

        return representation

class CageCreateSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    code = serializers.CharField(max_length=8,
                                 min_length=1)
    name = serializers.CharField(max_length=30,
                                 min_length=8)
    hability = serializers.BooleanField(default=False)
    observations = serializers.CharField(max_length=100,
                                         allow_blank=True,
                                         allow_null=True)

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        feed_animal = FeedAnimal.objects.create(animal_amount = 0)
        feed_animal_food = FeedAnimalFood.objects.create(animal_food_amount = 0)
        user = UserAsigned.objects.filter(id = user_data).first()

        cage = Cage.objects.create(feed_animal = feed_animal, feed_animal_food = feed_animal_food, user = user, **validated_data)
        return cage

class CageUpdateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=8,
                                 min_length=1)
    name = serializers.CharField(max_length=30,
                                 min_length=8)
    active = serializers.BooleanField()
    observations = serializers.CharField(max_length=100,
                                         allow_blank=True,
                                         allow_null=True)

    def update(self, instance, validated_data):
        instance.code = validated_data.get('code', instance.code)
        instance.name = validated_data.get('name', instance.name)
        instance.hability = validated_data.get('active', instance.hability)
        instance.observations = validated_data.get('observations', instance.observations)
        instance.save()
        return instance

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