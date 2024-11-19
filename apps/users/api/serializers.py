from random import choices

from rest_framework import serializers
from apps.users.models import User

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'username': instance.username,
            'firstname': instance.name,
            'lastname': instance.last_name,
            'observations': instance.observations,
            'tel': instance.tel,
            'role': 'USER' if instance.role == 0 else 'ADMIN',
            'is_active': instance.is_active,
            'changePassword': instance.changePassword,
            'changePasswordNextSession': instance.changePasswordNextSession
        }

class UpdateUser(serializers.Serializer):
    username = serializers.CharField(max_length=255,
                                     min_length=3)
    firstname = serializers.CharField(max_length=255,
                                      min_length=3)
    lastname = serializers.CharField(max_length=255,
                                      min_length=3)
    is_active = serializers.BooleanField(default=False)
    tel = serializers.CharField(max_length=10,
                                allow_null=True,
                                allow_blank=True)
    observations = serializers.CharField(max_length=100,
                                         allow_null=True,
                                         allow_blank=True)
    changePassword = serializers.BooleanField(default=False)
    changePasswordNextSession = serializers.BooleanField(default=False)
    # role = serializers.IntegerField(default=0)

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.firstname = validated_data['firstname']
        instance.last_name = validated_data['lastname']
        instance.is_active= validated_data['is_active']
        instance.tel = validated_data['tel']
        instance.observations = validated_data['observations']
        instance.changePassword = validated_data['changePassword']
        instance.changePasswordNextSession = validated_data['changePasswordNextSession']
        # instance.rol = validated_data['role']
        instance.save()
        return validated_data

class CreateUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(id = None, **validated_data)
        user.set_password(user.password)
        user.save()
        return user

class UpdatePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=20,
                                     min_length=8)

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return validated_data