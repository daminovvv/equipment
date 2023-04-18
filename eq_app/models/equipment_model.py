from django.db import models
from eq_app.models.equipment_type_model import EquipmentType


class Equipment(models.Model):
    type_code = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    sn = models.CharField(max_length=250, unique=True)
    comment = models.CharField(max_length=250)