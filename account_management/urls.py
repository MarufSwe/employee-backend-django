from django.urls import path, include
from account_management.views.vendor_views import AccountVendorViewSet
from account_management.views.shcedule_education_views import ScheduleEducationViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('acc-vendor', AccountVendorViewSet)
router.register('education', ScheduleEducationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('acc-vendor/', views.vendor_views.AccountVendorViewSet),
    path('education/', views.shcedule_education_views.ScheduleEducationViewSet),

]
