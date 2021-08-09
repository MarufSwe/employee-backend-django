from rest_framework import viewsets
from account_management.models import CreateMerchandise
from django_filters.rest_framework import DjangoFilterBackend
from account_management.serializers.merchandiser_serializers import MerchandiseSerializer
from account_management.paginations.paginations import CustomPageNumberPagination


class MerchandiseViewSet(viewsets.ModelViewSet):
    queryset = CreateMerchandise.objects.all()
    serializer_class = MerchandiseSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = CustomPageNumberPagination

