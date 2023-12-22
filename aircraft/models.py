from django.db import models
from abstract_models.models import AbstractBusy


class AircraftDescription(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to="aircraft/")


class AircraftCharacteristic(models.Model):
    assistant_pilot = models.BooleanField(default=False)


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
