from django.contrib.auth.admin import UserAdmin
from webauth.forms import EmployeeCreationForm, EmployeeChangeForm
from django.contrib import admin
from.models import Employee, EmployeeData


class CustomUserAdmin(UserAdmin):
    add_form = EmployeeCreationForm
    form = EmployeeChangeForm
    model = Employee
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}),
    )
    search_fields = ('email',)
    ordering = ('email',)


class EmployeeDataAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'surname', 'position']
    ordering = ['-created_at']
    search_fields = ['name', 'id']


admin.site.register(Employee, CustomUserAdmin)
admin.site.register(EmployeeData, EmployeeDataAdmin)
