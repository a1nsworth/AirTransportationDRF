from django.db import models

# Create your models here.


class AviationPersonnel(models.Model):
    class Role(models.TextChoices):
        PILOT = "PILOT"
        PILOT_ASSISTANT = "PILOT_ASSISTANT"
        STEWARD = "STEWARD"
        ENGINEER = "ENGINEER"

    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    role = models.CharField(max_length=100, choices=Role, null=True, default=None)
