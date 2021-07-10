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

    def __str__(self):
        return self.first_name


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

    def __str__(self):
        return self.name


class Inventory(models.Model):
    class Weight_Type(models.TextChoices):
        Ounce = 'ounce', ('Ounce')
        Pound = 'pound', ('Pound')
        Gram = 'gram', ('Gram')
        Kilogram = 'kg', ('Kilogram')

    product = models.CharField(max_length=50, null=False, blank=False)
    type = models.CharField(max_length=50, null=True, blank=True)
    type_option = models.CharField(max_length=30, null=True, blank=True)
    strain = models.CharField(max_length=30, null=True, blank=True)
    brand = models.CharField(max_length=30, null=True, blank=True)
    weight = models.CharField(max_length=20, null=True, blank=True)
    weight_type = models.CharField(max_length=20, blank=True, null=True, choices=Weight_Type.choices,
                                   default=Weight_Type.Pound)
    packaging = models.CharField(max_length=20, null=True, blank=True)
    price_per_unit = models.CharField(max_length=20, null=True, blank=True)
    metre_uid = models.CharField(max_length=30, null=True, blank=True)
    quantity_per_case = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.product


class AvailableInventory(models.Model):
    class Weight_Types(models.TextChoices):
        Ounce = 'ounce', ('Ounce')
        Pound = 'pound', ('Pound')
        Gram = 'gram', ('Gram')
        Kilogram = 'kg', ('Kilogram')

    product_name = models.CharField(max_length=100, null=False, blank=False)
    product_description = models.TextField(null=True, blank=True)
    quantity = models.CharField(default=0, max_length=5, null=True, blank=True)
    metre_uid = models.CharField(max_length=30, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    package_date = models.DateField(editable=True, blank=True, null=True)
    expiration_date = models.DateField(editable=True, blank=True, null=True)
    price_per_unit = models.CharField(max_length=20, null=True, blank=True)
    batch_id = models.CharField(max_length=20, null=True, blank=True)
    brand = models.CharField(max_length=30, null=True, blank=True)
    strain = models.CharField(max_length=30, null=True, blank=True)
    weight = models.CharField(max_length=20, null=True, blank=True)
    weight_type = models.CharField(max_length=20, blank=True, null=True, choices=Weight_Types.choices,
                                   default=Weight_Types.Pound)
    packaging = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.product_name


# Incoming Inventory Model
class IncomingInventory(models.Model):
    product = models.ForeignKey(AvailableInventory, on_delete=models.SET_NULL, null=True,
                                related_name='availableInventory_incomingInventory')
    quantity = models.CharField(default=0, max_length=5, null=True, blank=True)
    metric_uid = models.CharField(max_length=30, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)


# Incoming Inventory Model
class Orders(models.Model):
    class Excise_Text(models.TextChoices):
        Yes = 'yes', ('Yes')
        No = 'no', ('No')
    employee_id = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True,
                                    related_name='employee_order')
    vendor_id = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True,
                                  related_name='vendor_order')
    license_holder = models.CharField(max_length=100, null=True, blank=True)
    buyer_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    order = models.CharField(max_length=10, null=True, blank=True)
    product = models.ForeignKey(Inventory, on_delete=models.SET_NULL, null=True,
                                related_name='inventory_order')
    brand = models.CharField(max_length=50, null=True, blank=True)
    product_description = models.TextField(null=True, blank=True)
    price_per_unit = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.CharField(default=0, max_length=5, null=True, blank=True)
    excise_text = models.CharField(max_length=20, blank=True, null=True, choices=Excise_Text.choices,
                                   default=Excise_Text.Yes)
    payment_pickup_date = models.DateField(editable=True, blank=True, null=True)
    delivery_date = models.DateField(editable=True, blank=True, null=True)
    shipping_address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=50, null=True, blank=True)
    available_vendor_credit = models.CharField(max_length=10, null=True, blank=True)
    vendor_credit_used_today = models.CharField(max_length=10, null=True, blank=True)
    available_employee_credit = models.CharField(max_length=10, null=True, blank=True)
    employee_credit_used_today = models.CharField(max_length=10, null=True, blank=True)
    employee_discount = models.CharField(max_length=10, null=True, blank=True)
    sub_total = models.CharField(max_length=10, null=True, blank=True)
    total_taxes = models.CharField(max_length=10, null=True, blank=True)
    total = models.CharField(max_length=10, null=True, blank=True)
    total_due_today = models.CharField(max_length=10, null=True, blank=True)



