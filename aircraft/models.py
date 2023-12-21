from django.db import models


class Aircraft(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="aircraft/")
