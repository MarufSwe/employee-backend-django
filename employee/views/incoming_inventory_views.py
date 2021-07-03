from rest_framework import viewsets
from employee.models import IncomingInventory
from django_filters.rest_framework import DjangoFilterBackend
from employee.paginations.paginations import CustomPageNumberPagination
from employee.serializers.incoming_inventory_serializer import IncomingInventorySerializer


class IncomingInventoryViewSet(viewsets.ModelViewSet):
    queryset = IncomingInventory.objects.all()
    serializer_class = IncomingInventorySerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = CustomPageNumberPagination
