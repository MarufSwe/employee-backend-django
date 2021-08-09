from django.contrib import admin
from .models import *


# Vendor
@admin.register(AccountVendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['id', 'vendor_id', 'vendor_name', 'address', 'city', 'state', 'zip_code', 'license_no',
                    'seller_permit', 'phone', 'email', 'owner_name', 'point_of_contact', 'instagram',
                    'credit_allowance', 'collection', 'outstanding_credit', 'last_order']


@admin.register(ScheduleEducation)
class ScheduleEducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'phone', 'email', 'brand', 'date_time', 'no_of_hours']


@admin.register(CreateReport)
class CreateReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'product_location', 'brand_exposure', 'product_visibility', 'acc_vendor',]



@admin.register(CreateMerchandise)
class CreateMerchandiseAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'brand', 'type', 'description', 'quantity']