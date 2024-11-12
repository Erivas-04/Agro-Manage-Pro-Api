from rest_framework import serializers
from rest_framework.fields import IntegerField

from apps.animals.models import AnimalFood
from apps.company.models import UserAsigned


class AnimalFoodViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalFood
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'concentrate_name': instance.animal_food_name,
            'observations': instance.observations,
            'hability': instance.hability
        }

class AnimalFoodCreateUpdateSerializer(serializers.Serializer):
    user = serializers.IntegerField(allow_null=True)
    animal_food_name = serializers.CharField(max_length=20,
                                             min_length=4)
    observations = serializers.CharField(max_length=100,
                                         allow_null=True,
                                         allow_blank=True)
    hability = serializers.BooleanField()

    def create(self, validated_data):
        user_id = validated_data.pop('user')
        user = UserAsigned.objects.filter(id = user_id).first()

        return AnimalFood.objects.create(user = user, **validated_data)

    def update(self, instance, validated_data):
        instance.animal_food_name = validated_data.get('animal_food_name', instance.animal_food_name)
        instance.observations = validated_data.get('observations', instance.observations)
        instance.hability = validated_data.get('hability', instance.hability)
        instance.save()
        return validated_data