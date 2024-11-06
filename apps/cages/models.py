from django.core.validators import MinLengthValidator
from django.db import models
from apps.animals.models import Animal, AnimalFood
from apps.company.models import UserAsigned


class FeedAnimal(models.Model):
    id = models.BigAutoField("Id", primary_key=True, unique=True)
    animal_amount = models.IntegerField("Cantidad de animales")

class FeedAnimalFood(models.Model):
    id = models.BigAutoField("Id", primary_key=True, unique=True)
    animal_food_amount= models.FloatField("Cantidad de concentrado")

class Cage(models.Model):
    id = models.BigAutoField("Id",
                             primary_key=True,
                             unique=True)
    user = models.ForeignKey(UserAsigned,
                             on_delete=models.CASCADE)
    code = models.CharField("Codigo",
                            max_length=8,
                            validators=[MinLengthValidator(1)])
    name = models.CharField("Nombre",
                            max_length=30,
                            validators=[MinLengthValidator(4)])
    hability = models.BooleanField("Habilitado")
    observations = models.CharField("Observaciones",
                                    max_length=100,
                                    null=True,
                                    blank=True)


    feed_animal = models.OneToOneField(FeedAnimal,
                                      on_delete=models.CASCADE,
                                       null=True,
                                       blank=True)
    feed_animal_food = models.OneToOneField(FeedAnimalFood,
                                            on_delete=models.CASCADE,
                                       null=True,
                                       blank=True)
    animal = models.ForeignKey(Animal,
                               on_delete=models.CASCADE,
                                       null=True,
                                       blank=True)
    animal_food = models.ForeignKey(AnimalFood,
                                    on_delete=models.CASCADE,
                                       null=True,
                                       blank=True)


    class Meta:
        verbose_name = 'Corral'
        verbose_name_plural = 'Corrales'

    def __str__(self):
        return f"{self.name}, {self.code}"

