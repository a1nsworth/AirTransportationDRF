from django.db import models
from abstract_models.models import AbstractBusy

# Create your models here.


class AviationPersonnel(AbstractBusy):
    class Role(models.TextChoices):
        PILOT = "PILOT"
        PILOT_ASSISTANT = "PILOT_ASSISTANT"
        STEWARD = "STEWARD"
        ENGINEER = "ENGINEER"

    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    role = models.CharField(max_length=100, choices=Role, null=True, default=None)
    flight = models.ForeignKey(
        "flight.Flight",
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name="aviation_personnel",
    )

    def __str__(self):
        return f"{self.first_name} {self.second_name} | {self.role}"
