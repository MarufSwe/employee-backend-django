from rest_framework import serializers
from account_management.models import ScheduleEducation, AccountVendor
from django import forms


# Designation serializers
class AccountVendorSerializerForScheduleEducation(serializers.ModelSerializer):
    class Meta:
        model = AccountVendor
        fields = ('id', 'vendor_id', 'vendor_name')



# Schedule Education serializers
class ScheduleEducationSerializer(serializers.ModelSerializer):
    acc_vendor = AccountVendorSerializerForScheduleEducation(read_only=True)
    class Meta:
        model = ScheduleEducation
        fields = ('id', 'name', 'address', 'phone', 'email', 'brand', 'date_time', 'no_of_hours', 'acc_vendor')