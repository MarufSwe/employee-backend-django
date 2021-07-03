from rest_framework import serializers
from employee.models import AvailableInventory
from django import forms


# Designation serializers
class AvailableInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableInventory
        fields = ('id', 'product_name', 'product_description', 'quantity', 'metre_uid', 'location', 'type',
                  'package_date', 'expiration_date', 'price_per_unit', 'batch_id', 'brand', 'strain', 'weight',
                  'weight_type', 'packaging')
