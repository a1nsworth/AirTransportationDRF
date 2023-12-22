from rest_framework import viewsets, generics

from .models import Aircraft
from .serializers import (
    AircraftReadOnlySerializer,
    AircraftUpdateSerializer,
    AircraftDeleteSerializer,
    AircraftCreateSerializer,
)


class AircraftReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftReadOnlySerializer


class AircraftCreateAPIView(generics.CreateAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftCreateSerializer


class AircraftUpdateAPIView(generics.UpdateAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftUpdateSerializer


class AircraftDeleteAPIView(generics.DestroyAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftDeleteSerializer
