from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    phone_number = models.CharField(max_length=12, null=False)
    email = models.EmailField(max_length=100, null=True, default=None)
    telegram_id = models.CharField(max_length=100, null=True, default=None)
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
