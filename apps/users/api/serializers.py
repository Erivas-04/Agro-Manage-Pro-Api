from rest_framework import serializers
from apps.users.models import User

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'last_name', 'is_active', 'tel', 'observations', 'change_password', 'change_password_next_session']

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

class UpdatePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=20,
                                     min_length=8)

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return validated_data