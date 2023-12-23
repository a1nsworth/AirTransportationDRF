from rest_framework import status, permissions
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Client
from .serializers import (
    ClientReadOnlySerializer,
    ClientCreateSerializer,
    ClientUpdateSerializer,
)


class ClientReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientReadOnlySerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientCreateAPIView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer
    permission_classes = [permissions.AllowAny]


class ClientUpdateAPIView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClientDeleteAPIView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientReadOnlySerializer
    permission_classes = [permissions.IsAuthenticated]
