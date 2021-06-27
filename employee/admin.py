from django.contrib import admin
from .models import Employees, Vendor


# EmployeeAdmin
@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'position', 'employee_id', 'username',
                    'password', 'phone_no', 'discount_power', 'discount_power', 'discount_power',
                    'credit_allowance', 'commission']


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'vendor_id', 'name', 'address', 'city', 'state', 'zip_code', 'license_no',
                    'seller_permit', 'phone', 'email', 'owner_name', 'point_of_contact', 'instagram',
                    'credit_allowance', 'collection']


