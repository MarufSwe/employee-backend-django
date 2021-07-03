from rest_framework import serializers
from employee.models import IncomingInventory
from django import forms


# Designation serializers
class IncomingInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomingInventory
        fields = ('id', 'product', 'quantity', 'metric_uid', 'location',)
