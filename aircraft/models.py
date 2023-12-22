from django.db import models
from abstract_models.models import AbstractBusy


class AircraftDescription(models.Model):
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to="aircraft/", null=True, blank=True, default=None
    )


class AircraftCharacteristic(models.Model):
    capacity_peoples = models.PositiveSmallIntegerField(default=2)


class Aircraft(AbstractBusy):
    name = models.CharField(max_length=50)
    description = models.OneToOneField(
        "AircraftDescription",
        on_delete=models.CASCADE,
        related_name="aircraft",
    )
    characteristic = models.OneToOneField(
        "AircraftCharacteristic",
        on_delete=models.CASCADE,
        related_name="aircraft",
    )

    def __str__(self):
        return self.name
