from rest_framework import viewsets, status
from django.db import transaction
from rest_framework.response import Response
from account_management.models import ScheduleEducation
from django_filters.rest_framework import DjangoFilterBackend
from account_management.paginations.paginations import CustomPageNumberPagination
from account_management.serializers.schedule_education_serializers import ScheduleEducationCreateSerializer, \
    ScheduleEducationListSerializer


class ScheduleEducationViewSet(viewsets.ModelViewSet):
    queryset = ScheduleEducation.objects.all()
    serializer_class = ScheduleEducationListSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = CustomPageNumberPagination

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = ScheduleEducationCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
