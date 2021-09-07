from rest_framework import viewsets
from account_management.models import CustomInfo
from account_management.serializers.custom_info_serializers import CustomInfoListSerializer


class CustomInfoViewSet(viewsets.ModelViewSet):
    queryset = CustomInfo.objects.all()
    serializer_class = CustomInfoListSerializer

