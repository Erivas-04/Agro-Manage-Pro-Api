from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

class Input(models.Model):
    id = models.BigAutoField('Id',
                             primary_key = True,
                             unique = True)
    name = models.CharField('Nombre',
                            max_length=50,
                            validators=[MinLengthValidator(4)])
    price = models.FloatField('Precio',
                              validators=[MinValueValidator(0)])
