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


class AviationPersonnelCreateAPIView(generics.CreateAPIView):
    queryset = AviationPersonnel.objects.all()
    serializer_class = AviationPersonnelCreateSerializer


class AviationPersonnelUpdateAPIView(generics.UpdateAPIView):
    queryset = AviationPersonnel.objects.all()
    serializer_class = AviationPersonnelUpdateSerializer


class AviationPersonnelDeleteAPIView(generics.DestroyAPIView):
    queryset = AviationPersonnel.objects.all()
    serializer_class = AviationPersonnelDeleteSerializer
