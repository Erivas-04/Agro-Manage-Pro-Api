from rest_framework import serializers
from apps.animals.models import Animal
from apps.company.models import UserAsigned

class AnimalViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'id_user': instance.user.id,
            'animal_name': instance.animal_name,
            'observations': instance.observations,
            'hability': instance.hability
        }

class AnimalCreateUpdateSerializer(serializers.Serializer):
    user = serializers.IntegerField(allow_null=True)
    animal_name = serializers.CharField(max_length=15,
                                        min_length=4)
    observations = serializers.CharField(max_length=100,
                                         allow_blank=True,
                                         allow_null=True)
    hability = serializers.BooleanField()

    def create(self, validated_data):
        user_id = validated_data.pop('user')
        user = UserAsigned.objects.filter(id = user_id).first()

        return Animal.objects.create(user = user, **validated_data)

    def update(self, instance, validated_data):
        instance.animal_name = validated_data.get('animal_name', instance.animal_name)
        instance.observations = validated_data.get('observations', instance.observations)
        instance.hability = validated_data.get('hability', instance.hability)
        instance.save()
        return validated_data