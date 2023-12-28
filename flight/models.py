from django.db import models
from django.db.models import Q


class FlightComposition(models.Model):
    aircraft_id = models.OneToOneField(
        "aircraft.Aircraft",
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name="flight_aircraft",
        limit_choices_to={"busy": False},
    )
    client_id = models.OneToOneField(
        "client.Client",
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name="flight_client",
    )

    pilot_main = models.OneToOneField(
        "aviation_personnel.AviationPersonnel",
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name="flight_pilot",
        limit_choices_to={
            "role": "PILOT",
            "busy": False,
        },
    )
    pilot_assistant = models.ForeignKey(
        "aviation_personnel.AviationPersonnel",
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name="flight_pilot_assistant",
        limit_choices_to={
            "role": "PILOT_ASSISTANT",
            "busy": False,
        },
    )

    stewards = models.ManyToManyField(
        "aviation_personnel.AviationPersonnel",
        related_name="flight_composition",
        null=True,
        blank=True,
        default=None,
        limit_choices_to=Q(busy=False) & (Q(role="STEWARD") | Q(role="ENGINEER")),
    )


class Flight(models.Model):
    completed = models.BooleanField(null=True, default=None)

    composition = models.OneToOneField(
        FlightComposition,
        null=True,
        default=None,
        on_delete=models.CASCADE,
        related_name="flight",
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
