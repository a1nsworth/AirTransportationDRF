from rest_framework import viewsets
from rest_framework import permissions
from .models import AvailableCities
from .serializers import AvailableCitiesSerializer


class AvailableCitiesViewSet(viewsets.ModelViewSet):
    queryset = AvailableCities.objects.all()
    serializer_class = AvailableCitiesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
