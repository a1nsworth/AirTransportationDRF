from django.contrib.staticfiles.views import serve
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework import generics
from flight.models import Flight, FlightComposition
from .serializers import (
    RepresentationFlightSerializer,
    RepresentationFlightCompositionSerializer,
    CreateUpdateFlightSerializer,
    CreateUpdateFlightCompositionSerializer,
)


class FlightCompositionModelViewSet(viewsets.ModelViewSet):
    queryset = FlightComposition.objects.all()
    serializer_class = RepresentationFlightCompositionSerializer
    permission_classes = [permissions.IsAuthenticated]


class FlightReadOnlyAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = RepresentationFlightSerializer
    permission_classes = [permissions.IsAuthenticated]


class FlightDeleteAPIView(generics.DestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = RepresentationFlightSerializer
    permission_classes = [permissions.IsAuthenticated]


class FlightCreateAPIView(generics.CreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = CreateUpdateFlightSerializer
    permission_classes = [permissions.IsAuthenticated]


class FlightUpdateAPIView(generics.UpdateAPIView):
    queryset = Flight.objects.all()
    serializer_class = CreateUpdateFlightSerializer
    permission_classes = [permissions.IsAuthenticated]
