from django.urls import path, include
from account_management.views.vendor_views import AccountVendorViewSet
from account_management.views.shcedule_education_views import ScheduleEducationViewSet
from account_management.views.create_report_views import CreateReportViewSet
from account_management.views.merchandise_views import MerchandiseViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('acc-vendor', AccountVendorViewSet)
router.register('education', ScheduleEducationViewSet)
router.register('create-report', CreateReportViewSet)
router.register('merchandise', MerchandiseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('acc-vendor/', views.vendor_views.AccountVendorViewSet),
    path('education/', views.shcedule_education_views.ScheduleEducationViewSet),
    path('create-report/', views.create_report_views.CreateReportViewSet),
    path('merchandise/', views.merchandise_views.MerchandiseViewSet),

]
