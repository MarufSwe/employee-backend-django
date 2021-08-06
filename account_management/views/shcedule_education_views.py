from rest_framework import viewsets
from account_management.models import ScheduleEducation
from django_filters.rest_framework import DjangoFilterBackend
from account_management.serializers.schedule_education_serializers import ScheduleEducationSerializer
from account_management.paginations.paginations import CustomPageNumberPagination


class ScheduleEducationViewSet(viewsets.ModelViewSet):
    queryset = ScheduleEducation.objects.all()
    serializer_class = ScheduleEducationSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = CustomPageNumberPagination
