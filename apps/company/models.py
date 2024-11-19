from django.db import models
from django.core.validators import MinLengthValidator
from apps.users.models import User

class Company(models.Model):
    company_name = models.CharField('Nombre de empresa',
                                    max_length=30,
                                    validators=[MinLengthValidator(3)])
    hability = models.BooleanField('Habilitado',
                                   default=True)
    usernameExtension = models.CharField('Extension de empresa',
                                         max_length=10,
                                         validators=[MinLengthValidator(5)])
    address = models.CharField('Direccion',
                               max_length=25,
                               validators=[MinLengthValidator(6)])
    nit = models.CharField('NIT',
                           max_length=12,
                           validators=[MinLengthValidator(2)])
    owner = models.CharField('Propietario',
                             max_length=20,
                             validators=[MinLengthValidator(8)])
    tel = models.CharField('Telefono',
                           max_length=20,
                           null=True, blank=True)
    observations = models.CharField('Observaciones',
                                    max_length=100,
                                    null=True, blank=True)
    department = models.CharField('Departamento',
                                  max_length=25,
                                  null=True, blank=True)
    state = models.CharField('Municipio',
                             max_length=25,
                             null=True, blank=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return f'{self.company_name}'

class UserAsigned(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Asignacion'
        verbose_name_plural = 'Asignaciones'

    def save(self, *args, **kwargs):
        if not self.company_id or not Company.objects.filter(id=self.company_id).exists():
            raise ValueError("La empresa no existe")
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.name} de {self.company.company_name}'