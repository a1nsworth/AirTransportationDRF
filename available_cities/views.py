from rest_framework import viewsets
from .models import AvailableCities
from .serializers import AvailableCitiesSerializer


class AvailableCitiesViewSet(viewsets.ModelViewSet):
    queryset = AvailableCities.objects.all()
    serializer_class = AvailableCitiesSerializer
