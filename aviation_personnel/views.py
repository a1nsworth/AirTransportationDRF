from rest_framework import viewsets, generics, permissions

from .models import AviationPersonnel
from .serializers import (
    AviationPersonnelReadOnlyCreateSerializer,
    AviationPersonnelCreateSerializer,
    AviationPersonnelUpdateSerializer,
    AviationPersonnelDeleteSerializer,
)


class AviationPersonnelReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AviationPersonnel.objects.all()
    serializer_class = AviationPersonnelReadOnlyCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class AviationPersonnelCreateAPIView(generics.CreateAPIView):
    queryset = AviationPersonnel.objects.all()
    serializer_class = AviationPersonnelCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class AviationPersonnelUpdateAPIView(generics.UpdateAPIView):
    queryset = AviationPersonnel.objects.all()
    serializer_class = AviationPersonnelUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]


class AviationPersonnelDeleteAPIView(generics.DestroyAPIView):
    queryset = AviationPersonnel.objects.all()
    serializer_class = AviationPersonnelDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]
