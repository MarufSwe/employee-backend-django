from rest_framework import serializers
from employee.models import Employees
from django import forms


# Designation serializers
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = (
            'id', 'first_name', 'last_name', 'employee_id', 'position', 'username',
            'password', 'phone_no', 'discount_power', 'discount_power', 'discount_power',
            'credit_allowance', 'commission')
