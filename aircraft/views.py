from rest_framework import viewsets, generics, permissions

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
    permission_classes = [permissions.AllowAny]


class AircraftCreateAPIView(generics.CreateAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class AircraftUpdateAPIView(generics.UpdateAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]


class AircraftDeleteAPIView(generics.DestroyAPIView):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]
