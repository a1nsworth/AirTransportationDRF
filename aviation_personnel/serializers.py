from rest_framework import serializers
from .models import AviationPersonnel


class AviationPersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AviationPersonnel
        exclude = ["id"]
