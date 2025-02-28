# backend/service/views.py
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.db.models import Sum
import random  # only if you want to simulate revenue data
from .models import Component, Vehicle, Repair
from .serializers import ComponentSerializer, VehicleSerializer, RepairSerializer

# Component registration & listing
class ComponentListCreateView(generics.ListCreateAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

# Vehicle repair tracking: list and create vehicles
class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

# Repair creation (which includes issue reporting, component selection, and final price calculation)
class RepairListCreateView(generics.ListCreateAPIView):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer

# Revenue Graph endpoint: Aggregate revenue data over the past 30 days.
@api_view(['GET'])
def revenue_data(request):
    today = datetime.today().date()
    revenue_list = []
    for i in range(30):
        day = today - timedelta(days=i)
        repairs = Repair.objects.filter(created_at__date=day)
        day_total = repairs.aggregate(total=Sum('total_price'))['total'] or 0
        revenue_list.append({
            "date": day.strftime("%Y-%m-%d"),
            "revenue": float(day_total)
        })
    # Optionally sort by date ascending:
    revenue_list = sorted(revenue_list, key=lambda x: x["date"])
    return Response(revenue_list)



from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vehicle
from .serializers import VehicleSerializer

@api_view(['GET'])
def vehicle_list(request):
    try:
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=500)



@api_view(['POST'])
def process_payment(request, repair_id):
    try:
        repair = Repair.objects.get(id=repair_id)
        total_price = repair.total_price

        # Simulate payment logic (for now, just return success)
        return Response({"message": "Payment Successful", "amount_charged": total_price})
    
    except Repair.DoesNotExist:
        return Response({"error": "Repair not found"}, status=404)