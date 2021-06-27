from rest_framework import viewsets
from employee.models import Vendor
from employee.filters.filters import VendorFilter
from django_filters.rest_framework import DjangoFilterBackend
from employee.paginations.paginations import CustomPageNumberPagination
from employee.serializers.vendor_serializers import VendorSerializer


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all().order_by('name')
    serializer_class = VendorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = VendorFilter
    pagination_class = CustomPageNumberPagination
