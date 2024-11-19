from django.contrib import admin
from .models import UserAsigned

class UserAsignedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'company')

admin.site.register(UserAsigned, UserAsignedAdmin)