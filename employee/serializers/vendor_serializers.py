from rest_framework import serializers
from employee.models import Vendor
from django import forms


# Designation serializers
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('id', 'vendor_id', 'name', 'address', 'city', 'state', 'zip_code', 'license_no',
                    'seller_permit', 'phone', 'email', 'owner_name', 'point_of_contact', 'instagram',
                    'credit_allowance', 'collection')
