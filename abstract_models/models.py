from django.db import models


class AbstractBusy(models.Model):
    busy = models.BooleanField(default=False)

    class Meta:
        abstract = True
