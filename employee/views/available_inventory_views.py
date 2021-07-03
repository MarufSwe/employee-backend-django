from rest_framework import viewsets
from employee.models import AvailableInventory
from employee.filters.filters import AvailableInventoryFilter
from django_filters.rest_framework import DjangoFilterBackend
from employee.paginations.paginations import CustomPageNumberPagination
from employee.serializers.available_inventory_serializer import AvailableInventorySerializer


class AvailableInventoryViewSet(viewsets.ModelViewSet):
    queryset = AvailableInventory.objects.all().order_by('product_name')
    serializer_class = AvailableInventorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AvailableInventoryFilter
    pagination_class = CustomPageNumberPagination
