from rest_framework import viewsets
from account_management.models import AccountVendor
from django_filters.rest_framework import DjangoFilterBackend
from account_management.serializers.vendor_serializers import AccountVendorSerializer
from account_management.paginations.paginations import CustomPageNumberPagination


class AccountVendorViewSet(viewsets.ModelViewSet):
    queryset = AccountVendor.objects.all()
    serializer_class = AccountVendorSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = CustomPageNumberPagination

