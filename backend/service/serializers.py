# backend/service/serializers.py
from rest_framework import serializers
from .models import Component, Vehicle, Repair

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class RepairSerializer(serializers.ModelSerializer):
    # Use a primary key relation for components (or you could nest ComponentSerializer if desired)
    components = serializers.PrimaryKeyRelatedField(many=True, queryset=Component.objects.all())
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())

    class Meta:
        model = Repair
        fields = '__all__'
