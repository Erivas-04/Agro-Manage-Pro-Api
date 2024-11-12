from rest_framework import serializers
from apps.company.models import Company, UserAsigned
from apps.users.models import User

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
            'id': instance.user.id,
            'username': instance.user.username,
            'firstname': instance.user.firstname,
            'last_name': instance.user.last_name,
            'tel': instance.user.tel,
            'rol': instance.user.rol,
            'observations': instance.user.observations,
            'is_active': instance.user.is_active,
            'change_password': instance.user.changePassword,
            'change_password_next_session': instance.user.changePasswordNextSession,

        }