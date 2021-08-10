from rest_framework import viewsets, status
from account_management.models import OrderMerchandise
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from account_management.serializers.order_merchandise_serializers import OrderMerchandiseCreateSerializer, \
    OrderMerchandiseListSerializer
from account_management.paginations.paginations import CustomPageNumberPagination
from django.db import transaction


class OrderMerchandiseViewSet(viewsets.ModelViewSet):
    queryset = OrderMerchandise.objects.all()
    serializer_class = OrderMerchandiseListSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = CustomPageNumberPagination

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = OrderMerchandiseCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
