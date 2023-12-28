from django.db.models import QuerySet
from django.http import HttpResponse
from import_export import resources
from rest_framework import status
from typing import Type


def export_queryset(
    resource_model: Type[resources.ModelResource],
    queryset: QuerySet,
    filename: str,
    fmt: str,
) -> HttpResponse:
    dataset = resource_model().export(queryset)
    match fmt:
        case "xlc":
            dataset = dataset.xls
        case "csv":
            dataset = dataset.csv
        case "json":
            dataset = dataset.json
        case _:
            return HttpResponse(
                status=status.HTTP_400_BAD_REQUEST, content="Invalid format"
            )
    response = HttpResponse(
        content=dataset,
        content_type=f"{fmt}",
    )
    response["Content-Disposition"] = f"attachment; filename={filename}.{fmt}"
    return response
