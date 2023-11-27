from django.contrib import admin
from .models import User, Category, Service, Appointment, Employee
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'full_name', 'phone_number', 'address', 'age', 'pin_code')
    search_fields = ('username', 'full_name', 'phone_number', 'address', 'age', 'pin_code')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('full_name', 'phone_number', 'address', 'age', 'pin_code')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'phone_number', 'address', 'age', 'pin_code'),
        }),
    )

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Employee)

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Appointment)
# class AppointmentAdmin(admin.ModelAdmin):
#     pass

# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     pass