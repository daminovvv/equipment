from django.db import models


class EquipmentType(models.Model):
    name = models.CharField(max_length=100)
    mask_sn = models.CharField(max_length=100)