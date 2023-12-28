from import_export import resources
from rest_framework import viewsets, generics, views

from utils import export
from .models import Aircraft
from .serializers import (
    AircraftReadOnlySerializer,
    AircraftUpdateSerializer,
    AircraftDeleteSerializer,
    AircraftCreateSerializer,
)


class AircraftExportAPIView(views.APIView):
    def post(self, request, fmt):
        queryset = Aircraft.objects
        if (
            request.data.get("sql_request") is None
            or request.data.get("sql_request") == " "
        ):
            queryset = queryset.all()
        else:
            queryset = queryset.raw(request.data.get("sql_request"))

        return export.export_queryset(
            resources.modelresource_factory(model=Aircraft),
            queryset,
            Aircraft._meta.model_name,
            fmt,
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
