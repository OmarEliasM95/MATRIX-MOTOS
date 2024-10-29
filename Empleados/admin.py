from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Empleado

class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name' ,'dni','dirección', ]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name','dni', 'dirección','telefono', 'email', )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = ((None, {'fields':('username','first_name', 'last_name','dni', 'dirección','telefono', 'email', 'password1', 'password2')}),)
admin.site.register(Empleado, CustomUserAdmin)