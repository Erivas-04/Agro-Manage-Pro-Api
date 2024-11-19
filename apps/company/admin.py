from django.contrib import admin
from .models import UserAsigned, Company


class UserAsignedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'company')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name',)

admin.site.register(UserAsigned, UserAsignedAdmin)
admin.site.register(Company, CompanyAdmin)