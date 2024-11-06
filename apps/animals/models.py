from django.db import models
from django.core.validators import MinLengthValidator
from apps.company.models import UserAsigned


class Animal(models.Model):
    id = models.BigAutoField("Id",
                             primary_key=True,
                             unique=True)
    user = models.ForeignKey(UserAsigned, on_delete=models.CASCADE)
    animal_name = models.CharField("Nombre de animal",
                                   max_length=15,
                                   validators=[MinLengthValidator(4)])
    observations = models.CharField("Observaciones",
                                    max_length=100,
                                    null=True,
                                    blank=True)
    hability = models.BooleanField("Habilitado")

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'

    def __str__(self):
        return f"Animal: {self.animal_name}"


class AnimalFood(models.Model):
    id = models.BigAutoField("Id",
                             primary_key=True,
                             unique=True)
    user = models.ForeignKey(UserAsigned,
                             on_delete=models.CASCADE)
    animal_food_name = models.CharField("Nombre de concentrado",
                                        max_length=20,
                                        validators=[MinLengthValidator(4)])
    observations = models.CharField("Observaciones",
                                    max_length=100,
                                    null=True,
                                    blank=True)
    hability = models.BooleanField("Habilitado")

    class Meta:
        verbose_name = 'Concentrado'
        verbose_name_plural = 'Concentrados'

    def __str__(self):
        return f"{self.animal_food_name}"