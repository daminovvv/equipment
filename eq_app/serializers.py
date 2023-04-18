from rest_framework import serializers
from eq_app.models import Equipment, EquipmentType


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"
