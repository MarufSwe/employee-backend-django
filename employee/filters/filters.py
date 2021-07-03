from django_filters import rest_framework as filters
from employee.models import Employees, Vendor, Inventory, AvailableInventory


# VendorFilter Filter
class EmployeeFilter(filters.FilterSet):
    employee_id = filters.CharFilter(field_name="employee_id", lookup_expr="icontains")

    class Meta:
        model = Employees
        fields = ['employee_id']


# VendorFilter Filter
class VendorFilter(filters.FilterSet):
    vendor_id = filters.CharFilter(field_name="vendor_id", lookup_expr="icontains")

    class Meta:
        model = Vendor
        fields = ['vendor_id']


# VendorFilter Filter
class InventoryFilter(filters.FilterSet):
    strain = filters.CharFilter(field_name="strain", lookup_expr="icontains")

    class Meta:
        model = Inventory
        fields = ['strain']


# VendorFilter Filter
class AvailableInventoryFilter(filters.FilterSet):
    metre_uid = filters.CharFilter(field_name="metre_uid", lookup_expr="icontains")

    class Meta:
        model = AvailableInventory
        fields = ['metre_uid']
