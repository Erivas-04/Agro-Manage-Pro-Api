from rest_framework import serializers
from apps.company.models import Company, UserAsigned

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class UserAsignedSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAsigned
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'username': instance.user.username,
            'name': instance.user.name,
            'last_name': instance.user.last_name,
            'is_active': instance.user.is_active,
            'tel': instance.user.tel,
            'observations': instance.user.observations,
            'change_password': instance.user.change_password,
            'change_password_next_session': instance.user.change_password_next_session,

        }