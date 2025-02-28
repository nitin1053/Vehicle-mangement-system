# backend/service/urls.py
from django.urls import path
from .views import (
    ComponentListCreateView,
    VehicleListCreateView,
    RepairListCreateView,
    process_payment,
    revenue_data,
)

urlpatterns = [
    path('components/', ComponentListCreateView.as_view(), name='component-list'),
    path('vehicles/', VehicleListCreateView.as_view(), name='vehicle-list'),
    # path('repairs/', RepairListCreateView.as_view(), name='repair-list'),
    path('repairs/<int:repair_id>/pay/', process_payment, name='process_payment'),
    path('revenue/', revenue_data, name='revenue-data'),
]
