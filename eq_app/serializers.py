import re
from django.core.validators import RegexValidator
from rest_framework import serializers
from eq_app.models import Equipment, EquipmentType


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        exclude = ['deleted']

    def validate(self, data):
        """Validates SN according to mask of equipment type"""
        related_data = data['type_code'].mask_sn
        translate = {
            "N": "([0-9])",
            "A": "([A-Z])",
            "a": "([a-z])",
            "X": "([A-Z]|[0-9])",
            "Z": "(-|_|@)"
        }
        sn_pattern = re.compile(r"^{}$".format(''.join(translate[letter] for letter in related_data)))

        regex_validator = RegexValidator(
            regex=sn_pattern,
            message=f"Serial number does not match following mask of equipment type: {related_data}, "
                    f"where N - number, A - uppercase letter, a - lowercase letter, "
                    f"X - number or uppercase letter, Z - symbol from the list -,_,@",
        )

        regex_validator(data['sn'])
        return data


class EquipmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentType
        fields = '__all__'
