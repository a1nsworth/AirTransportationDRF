from rest_framework import serializers
from .models import AvailableCities


class AvailableCitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableCities
        fields = "__all__"
