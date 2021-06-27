from django.db import models
from django.contrib.auth.models import User


# Employee Model
class Employees(models.Model):
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    position = models.CharField(max_length=25, null=True, blank=True)
    employee_id = models.CharField(max_length=20, unique=True, blank=False, null=False)
    username = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=25, null=False, blank=False)
    phone_no = models.CharField(max_length=20, null=True, blank=True)
    discount_power = models.CharField(max_length=6, null=True, blank=True)
    credit_allowance = models.CharField(max_length=6, null=True, blank=True)
    commission = models.CharField(max_length=6, null=True, blank=True)


# Vendor Model
class Vendor(models.Model):
    class State(models.TextChoices):
        Dhaka = 'dhaka', ('Dhaka')
        Chattogram = 'chattogram', ('Chattogram')
        Rajshahi = 'rajshahi', ('Rajshahi')
        Barishal = 'barishal', ('Barishal')
        Khulna = 'khulna', ('Khulna')
        Rangpur = 'rangpur', ('Rangpur')
        Mymensingh = 'mymensingh', ('Mymensingh')
        Sylhet = 'sylhet', ('Sylhet')

    vendor_id = models.CharField(max_length=20, unique=True, blank=False, null=False)
    name = models.CharField(max_length=30, null=False, blank=False)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True, choices=State.choices, default=State.Dhaka)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    license_no = models.CharField(max_length=50, blank=True, null=True)
    seller_permit = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    owner_name = models.CharField(max_length=30, blank=True, null=True)
    point_of_contact = models.CharField(max_length=30, blank=True, null=True)
    instagram = models.CharField(max_length=30, blank=True, null=True)
    credit_allowance = models.CharField(max_length=6, null=True, blank=True)
    collection = models.BooleanField(default=True, blank=True, null=True)