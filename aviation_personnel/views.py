from rest_framework import viewsets, generics, views
from import_export import resources
from utils import export
from .models import AviationPersonnel
from .serializers import (
    AviationPersonnelReadOnlyCreateSerializer,
    AviationPersonnelCreateSerializer,
    AviationPersonnelUpdateSerializer,
    AviationPersonnelDeleteSerializer,
)


class AviationPersonnelExportAPIView(views.APIView):
    def post(self, request, fmt):
        queryset = AviationPersonnel.objects
        if (
            request.data.get("sql_request") is None
            or request.data.get("sql_request") == " "
        ):
            queryset = queryset.all()
        else:
            queryset = queryset.raw(request.data.get("sql_request"))

        return export.export_queryset(
            resources.modelresource_factory(model=AviationPersonnel),
            queryset,
            AviationPersonnel._meta.model_name,
            fmt,
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
