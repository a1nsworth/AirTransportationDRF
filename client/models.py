from abstract_models.models import AbstractBusy
from django.db import models


class ClientOrder(models.Model):
    desired_aircraft = models.ForeignKey(
        "aircraft.Aircraft",
        null=True,
        default=None,
        blank=True,
        on_delete=models.SET_NULL,
    )
    departure_date = models.DateField(null=True, default=None)
    arrival_date = models.DateField(null=True, default=None)
    departure_city = models.ForeignKey(
        "available_cities.AvailableCities",
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name="client_departure_city",
    )
    arrival_city = models.ForeignKey(
        "available_cities.AvailableCities",
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name="client_arrival_city",
    )


class Client(AbstractBusy):
    first_name = models.CharField(max_length=30, null=False)
    phone_number = models.CharField(max_length=12, null=False)
    email = models.EmailField(max_length=100, null=True, default=None)
    telegram_id = models.CharField(max_length=100, null=True, default=None)
    order = models.OneToOneField(
        ClientOrder,
        on_delete=models.CASCADE,
        related_name="client",
        unique=True,
    )

    def __str__(self):
        return f"{self.first_name} | {self.phone_number}"
