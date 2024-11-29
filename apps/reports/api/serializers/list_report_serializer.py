from rest_framework import serializers
from apps.reports.models import AsigAnimalMove, AsigAnimalFoodMove

class ReportAnimalMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsigAnimalMove
        fields = '__all__'

    def to_representation(self, instance):
        return instance

class ReportAnimalFoodMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsigAnimalFoodMove
        fields = '__all__'

    def to_representation(self, instance):
        return instance

