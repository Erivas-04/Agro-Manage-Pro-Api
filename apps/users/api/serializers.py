from rest_framework import serializers
from apps.users.models import User

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'last_name', 'is_active', 'tel', 'observations', 'change_password', 'change_password_next_session']

    # def to_representation(self, instance):
    #     return {
    #         'id': instance['id'],
    #         'Usuario': instance['username'],
    #         'Clave': instance['password'],
    #         'Nombres': instance['name'],
    #         'Apellidos': instance['last_name'],
    #         'Habilitado': instance['is_active'],
    #         'Telefono': instance['tel'],
    #         'Observaciones': instance['observations'],
    #         'Cambiar contraseña': instance['change_password'],
    #         'Cambiar contraseña en siguiente sesion': instance['change_password_next_session']
    #     }

class UserModifySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user