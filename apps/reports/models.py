from django.db import models
from django.core.validators import MinValueValidator
from django.conf import settings

class AnimalMove(models.Model):
    id = models.BigAutoField('id',
                             primary_key = True,
                             unique=True)
    user = models.ForeignKey('company.UserAsigned',
                             on_delete=models.CASCADE)
    movement_date = models.DateTimeField(auto_now_add=True, blank=True)
    weight = models.FloatField('Peso',
                               validators=[MinValueValidator(0)])
    age = models.FloatField('Edad',
                            validators=[MinValueValidator(0)])
    amount_animals = models.IntegerField('Cantidad de animales',
                                         default=1)
    type = models.PositiveSmallIntegerField('Tipo de movimiento',choices=settings.ANIMAL_MOVE_OPTIONS)

    class Meta:
        verbose_name = 'Movimiento de animal'
        verbose_name_plural = 'Movimientos de animales'

    def __str__(self):
        return (f'usuario: {self.user}, movement_date: {self.movement_date}, weight: {self.weight}, age: {self.age},'
                f'amount_animals: {self.amount_animals}, type: {self.type}')

class AnimalFoodMove(models.Model):
    id = models.BigAutoField('id',
                             primary_key = True,
                             unique=True)
    type = models.PositiveSmallIntegerField('Tipo de movimiento',choices=settings.ANIMAL_FOOD_MOVE_OPTIONS)
    user = models.ForeignKey('company.UserAsigned',
                             on_delete=models.CASCADE)
    amount = models.FloatField('Cantidad',
                               validators=[MinValueValidator(0)])
    date = models.DateTimeField('Fecha de registro',
                                auto_now_add=True)

    class Meta:
        verbose_name = 'Movimiento de concentrado'
        verbose_name_plural = 'Movimientos de concentrados'

    def __str__(self):
        return f'concentrado, tipo:{self.type}, fecha: {self.date}'

class AsigAnimalMove(models.Model):
    id = models.BigAutoField('id',
                             primary_key = True,
                             unique=True)
    animal_move = models.OneToOneField('AnimalMove',
                                    on_delete=models.CASCADE)
    cage = models.ForeignKey('cages.Cage',
                             on_delete=models.CASCADE)

class AsigAnimalFoodMove(models.Model):
    id = models.BigAutoField('id',
                             primary_key = True,
                             unique=True)
    animalfood_move = models.OneToOneField('AnimalFoodMove',
                                        on_delete=models.CASCADE)
    cage = models.ForeignKey('cages.Cage',
                             on_delete=models.CASCADE)