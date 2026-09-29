from django.contrib import admin
from .models import Employee, Department

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = (
        'employee_id',
        'first_name',
        'last_name',
        'email',
        'department',
        'designation',
        'status',
    )

    search_fields = (
        'employee_id',
        'first_name',
        'last_name',
        'email',
    )

    list_filter = (
        'department',
        'status',
    )