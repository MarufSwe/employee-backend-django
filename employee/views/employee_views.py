from rest_framework import viewsets
from employee.models import Employees
from employee.filters.filters import EmployeeFilter
from django_filters.rest_framework import DjangoFilterBackend
from employee.paginations.paginations import CustomPageNumberPagination
from employee.serializers.employee_serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all().order_by('first_name')
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter
    pagination_class = CustomPageNumberPagination
