from django.urls import path, include
from employee.views.employee_views import EmployeeViewSet
from employee.views.vendor_views import VendorViewSet
from employee.views.inventory_views import InventoryViewSet
from employee.views.available_inventory_views import AvailableInventoryViewSet
from employee.views.incoming_inventory_views import IncomingInventoryViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('employee', EmployeeViewSet)
router.register('vendor', VendorViewSet)
router.register('inventory', InventoryViewSet)
router.register('available-inventory', AvailableInventoryViewSet)
router.register('incoming-inventory', IncomingInventoryViewSet)

app_name = 'polls'
urlpatterns = [
    path('', include(router.urls)),
    path('employee/', views.employee_views.EmployeeViewSet),
    path('vendor/', views.vendor_views.VendorViewSet),
    path('inventory/', views.inventory_views.InventoryViewSet),
    # path('available-inventory/', views.available_inventory_views.AvailableInventoryViewSet),
    # path('available-inventory/', views.incoming_inventory_views.IncomingInventoryViewSet),

]
