from rest_framework import viewsets, views
from import_export import resources

from utils import export
from .models import AvailableCities
from .serializers import AvailableCitiesSerializer


class AvailableCitiesExportAPIView(views.APIView):
    def post(self, request, fmt):
        queryset = AvailableCities.objects
        if (
            request.data.get("sql_request") is None
            or request.data.get("sql_request") == " "
        ):
            queryset = queryset.all()
        else:
            queryset = queryset.raw(request.data.get("sql_request"))

        return export.export_queryset(
            resources.modelresource_factory(model=AvailableCities),
            queryset,
            AvailableCities._meta.model_name,
            fmt,
        )


class AvailableCitiesViewSet(viewsets.ModelViewSet):
    queryset = AvailableCities.objects.all()
    serializer_class = AvailableCitiesSerializer
