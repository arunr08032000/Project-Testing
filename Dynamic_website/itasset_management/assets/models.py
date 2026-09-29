from django.db import models
from employees.models import Employee

# Create your models here.
class Asset(models.Model):

    ASSET_TYPES = [
        ('LAPTOP', 'Laptop'),
        ('DESKTOP', 'Desktop'),
        ('MONITOR', 'Monitor'),
        ('PRINTER', 'Printer'),
        ('MOBILE', 'Mobile'),
        ('NETWORK', 'Network Device'),
        ('SERVER', 'Server'),
        ('OTHER', 'Other'),
    ]

    STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('ASSIGNED', 'Assigned'),
        ('REPAIR', 'Under Repair'),
        ('SCRAPPED', 'Scrapped'),
        ('LOST', 'Lost'),
    ]

    asset_id = models.CharField(
        max_length=50,
        unique=True
    )

    asset_type = models.CharField(
        max_length=30,
        choices=ASSET_TYPES
    )

    manufacturer = models.CharField(
        max_length=100,
        blank=True
    )

    model = models.CharField(
        max_length=100,
        blank=True
    )

    serial_number = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True
    )

    purchase_date = models.DateField(
        null=True,
        blank=True
    )

    warranty_expiry = models.DateField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='AVAILABLE'
    )

    location = models.CharField(
        max_length=100,
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.asset_id} - {self.asset_type}"


class AssetAssignment(models.Model):

    STATUS_CHOICES = [
        ('ASSIGNED', 'Assigned'),
        ('RETURNED', 'Returned'),
    ]

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    assigned_date = models.DateField(
        auto_now_add=True
    )

    returned_date = models.DateField(
        null=True,
        blank=True
    )

    condition_on_assignment = models.CharField(
        max_length=200,
        blank=True
    )

    condition_on_return = models.CharField(
        max_length=200,
        blank=True
    )

    remarks = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ASSIGNED'
    )

    def __str__(self):
        return f"{self.asset.asset_id} → {self.employee.employee_id}"