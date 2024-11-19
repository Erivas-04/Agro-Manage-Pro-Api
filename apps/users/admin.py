from django.contrib import admin
from apps.users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'firstname', 'last_name')

admin.site.register(User, UserAdmin)