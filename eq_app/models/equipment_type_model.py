from django.db import models
from django.core.validators import RegexValidator


class EquipmentType(models.Model):
    name = models.CharField(max_length=100)
    mask_sn_validator = RegexValidator(
        regex='^[N, A, a, X, Z]{10}$',
        message='Mask SN should contain only N, A, a, X, Z. 10 digits allowed.'
    )
    mask_sn = models.CharField(max_length=10, validators=[mask_sn_validator])
