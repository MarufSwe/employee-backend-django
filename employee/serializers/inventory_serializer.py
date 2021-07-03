from rest_framework import serializers
from employee.models import Inventory
from django import forms


# Designation serializers
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id', 'product', 'type', 'type_option', 'strain', 'brand', 'weight', 'weight_type', 'packaging',
                  'price_per_unit', 'metre_uid', 'quantity_per_case')
