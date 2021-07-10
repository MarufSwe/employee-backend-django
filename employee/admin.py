from django.contrib import admin
from .models import *


# EmployeeAdmin
@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'position', 'employee_id', 'username',
                    'password', 'phone_no', 'discount_power', 'discount_power', 'discount_power',
                    'credit_allowance', 'commission']


# Vendor
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'vendor_id', 'name', 'address', 'city', 'state', 'zip_code', 'license_no',
                    'seller_permit', 'phone', 'email', 'owner_name', 'point_of_contact', 'instagram',
                    'credit_allowance', 'collection']


# Vendor
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'type', 'type_option', 'strain', 'brand', 'weight', 'weight_type', 'packaging',
                    'price_per_unit', 'metre_uid', 'quantity_per_case']


# AvailableInventory
@admin.register(AvailableInventory)
class AvailableInventoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_description', 'quantity', 'metre_uid', 'location', 'type',
                    'package_date', 'expiration_date', 'price_per_unit', 'batch_id', 'brand', 'strain', 'weight',
                    'weight_type', 'packaging']



# IncomingInventory
@admin.register(IncomingInventory)
class IncomingInventoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'quantity', 'metric_uid', 'location',]


# IncomingInventory
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee_id', 'vendor_id', 'license_holder', 'buyer_name', 'phone', 'email', 'order',
                    'product', 'brand', 'product_description', 'price_per_unit', 'quantity', 'excise_text', 'payment_pickup_date',
                    'delivery_date', 'shipping_address', 'city', 'state', 'zip_code', 'available_vendor_credit',
                    'vendor_credit_used_today', 'available_employee_credit', 'employee_credit_used_today', 'employee_discount',
                    'sub_total', 'total_taxes', 'total', 'total_due_today']
