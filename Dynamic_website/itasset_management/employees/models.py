from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):

    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('RESIGNED', 'Resigned'),
    ]

    employee_id = models.CharField(
        max_length=50,
        unique=True
    )

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(
        max_length=100,
        blank=True
    )

    email = models.EmailField(unique=True)

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    designation = models.CharField(
        max_length=100,
        blank=True
    )

    location = models.CharField(
        max_length=100,
        blank=True
    )

    joining_date = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ACTIVE'
    )

    photo = models.ImageField(
        upload_to='employee_photos/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.employee_id} - {self.first_name}"