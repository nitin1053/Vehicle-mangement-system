# backend/service/models.py
from django.db import models

class Component(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # repair pricing or purchase price

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    issue_description = models.TextField(null=True, blank=True) 

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

SERVICE_TYPE_CHOICES = [
    ('new', 'New Component'),
    ('repair', 'Repair Service'),
]
# from django.db import models

# class Repair(models.Model):
#     vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, related_name='repairs')
#     issue_description = models.TextField()
#     service_type = models.CharField(max_length=10, choices=[('new', 'New Component'), ('repair', 'Repair Service')], default='new')
#     components = models.ManyToManyField('Component', blank=True)
#     labor_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)  # Save first to get an ID

#         # Ensure total price is calculated AFTER saving
#         if self.pk:
#             component_total = sum(c.price for c in self.components.all())
#             self.total_price = self.labor_cost + component_total
#             super().save(update_fields=['total_price'])

# ffrom django.db import models

class Repair(models.Model):
    vehicle = models.ForeignKey("Vehicle", on_delete=models.CASCADE)
    issue_description = models.TextField()
    service_type = models.CharField(max_length=10, choices=[("new", "New"), ("repair", "Repair")])
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2)
    components = models.ManyToManyField("Component", blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Ensure this exists!

    def save(self, *args, **kwargs):
        self.total_price = self.labor_cost + sum(c.price for c in self.components.all())
        super().save(*args, **kwargs)
