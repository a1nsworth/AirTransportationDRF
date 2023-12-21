from rest_framework import viewsets
from .serializers import AircraftSerializer
from .models import Aircraft


class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
