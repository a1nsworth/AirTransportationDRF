from django.shortcuts import render
from rest_framework import viewsets
from .models import AviationPersonnel
from .serializers import AviationPersonnelSerializer


class AviationPersonnelViewSet(viewsets.ModelViewSet):
    queryset = AviationPersonnel.objects.all()
    serializer_class = AviationPersonnelSerializer
