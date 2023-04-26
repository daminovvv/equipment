from rest_framework import serializers

from eq_app.models import Equipment
from eq_app.models import EquipmentType
from eq_app.services import validate_sn


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        exclude = ["deleted"]

    def validate(self, data):
        """Validates SN according to mask of equipment type"""
        validate_sn(data["sn"], data["type_code"].mask_sn)
        return data


class EquipmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentType
        fields = "__all__"
