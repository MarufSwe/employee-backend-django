from django.urls import path, include
from employee.views.employee_views import EmployeeViewSet
from employee.views.vendor_views import VendorViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('employee', EmployeeViewSet)
router.register('vendor', VendorViewSet)

app_name = 'polls'
urlpatterns = [
    path('', include(router.urls)),
    path('employee/', views.employee_views.EmployeeViewSet),
    path('vendor/', views.vendor_views.VendorViewSet),

]
