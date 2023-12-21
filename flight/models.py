from django.db import models


class Flight(models.Model):
    aircraft_id = models.ForeignKey(
        "aircraft.Aircraft",
        null=False,
        on_delete=models.DO_NOTHING,
        related_name="flight_aircraft",
    )

    departure_date = models.DateField(null=True, default=None)
    arrival_date = models.DateField(null=True, default=None)
    departure_city = models.ForeignKey(
        "available_cities.AvailableCities",
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name="flight_departure_city",
    )
    arrival_city = models.ForeignKey(
        "available_cities.AvailableCities",
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name="flight_arrival_city",
    )
