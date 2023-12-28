from rest_framework import generics, views, viewsets
from import_export import resources
from utils import export
from .models import Client
from .serializers import (
    ClientReadOnlySerializer,
    ClientCreateSerializer,
    ClientUpdateSerializer,
)


class ClientExportAPIView(views.APIView):
    def post(self, request, fmt):
        queryset = Client.objects
        if (
            request.data.get("sql_request") is None
            or request.data.get("sql_request") == " "
        ):
            queryset = queryset.all()
        else:
            queryset = queryset.raw(request.data.get("sql_request"))

        return export.export_queryset(
            resources.modelresource_factory(model=Client),
            queryset,
            Client._meta.model_name,
            fmt,
        )


class ClientReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientReadOnlySerializer


class ClientCreateAPIView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer


class ClientUpdateAPIView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientUpdateSerializer


class ClientDeleteAPIView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientReadOnlySerializer
