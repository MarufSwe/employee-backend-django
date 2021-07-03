from rest_framework import viewsets
from employee.models import Inventory
from employee.filters.filters import InventoryFilter
from django_filters.rest_framework import DjangoFilterBackend
from employee.paginations.paginations import CustomPageNumberPagination
from employee.serializers.inventory_serializer import InventorySerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all().order_by('product')
    serializer_class = InventorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = InventoryFilter
    pagination_class = CustomPageNumberPagination
