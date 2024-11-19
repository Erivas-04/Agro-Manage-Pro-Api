from operator import truediv
from random import choices

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models import Model
from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):
    def _create_user(self, username, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = None,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            role = 1,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, name,last_name, password=None, **extra_fields):
        return self._create_user(username, name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, name,last_name, password=None, **extra_fields):
        return self._create_user(username, name,last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique = True)
    name = models.CharField('Nombres', max_length = 255)
    last_name = models.CharField('Apellidos', max_length = 255)
    email = models.EmailField('Correo_Electrónico',max_length = 255, unique = True, null = True, blank=True)
    image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
    is_active = models.BooleanField('Habilitado',default = True)
    is_staff = models.BooleanField('Ingreso a api',default = False)
    historical = HistoricalRecords()
    objects = UserManager()

    tel = models.CharField('Telfono', max_length=10, null=True, blank=True)
    observations = models.CharField('Observaciones', max_length=100, null=True, blank=True)
    changePassword = models.BooleanField('Cambiar contraseña',default=False)
    changePasswordNextSession = models.BooleanField('Cambiar contraseña en el siguiente inicio de sesion',
                                                       default=False)
    ROLES = (
        (0, 'USER'),
        (1, 'ADMIN')
    )
    role = models.PositiveSmallIntegerField(choices = ROLES)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','last_name']

    def __str__(self):
        return f'{self.name} {self.last_name}'