from rest_framework import viewsets, generics, views
from import_export import resources
from flight.models import Flight, FlightComposition
from utils import export
from .serializers import (
    RepresentationFlightSerializer,
    RepresentationFlightCompositionSerializer,
    CreateCreateUpdateFlightSerializer,
)


class FlightExportAPIView(views.APIView):
    def post(self, request, fmt):
        queryset = Flight.objects
        if (
            request.data.get("sql_request") is None
            or request.data.get("sql_request") == " "
        ):
            queryset = queryset.all()
        else:
            queryset = queryset.raw(request.data.get("sql_request"))

        return export.export_queryset(
            resources.modelresource_factory(model=Flight),
            queryset,
            Flight._meta.model_name,
            fmt,
        )


class FlightCompositionModelViewSet(viewsets.ModelViewSet):
    queryset = FlightComposition.objects.all()
    serializer_class = RepresentationFlightCompositionSerializer


class FlightReadOnlyAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = RepresentationFlightSerializer


class FlightDeleteAPIView(generics.DestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = RepresentationFlightSerializer


class FlightCreateAPIView(generics.CreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = CreateCreateUpdateFlightSerializer


class FlightUpdateAPIView(generics.UpdateAPIView):
    queryset = Flight.objects.all()
    serializer_class = CreateCreateUpdateFlightSerializer
