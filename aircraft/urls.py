from django.urls import path

from .views import (
    AircraftReadOnlyViewSet,
    AircraftUpdateAPIView,
    AircraftCreateAPIView,
    AircraftDeleteAPIView,
    AircraftExportAPIView,
)

urlpatterns = [
    path("aircraft/", AircraftReadOnlyViewSet.as_view({"get": "list"})),
    path("aircraft/export/<str:fmt>/", AircraftExportAPIView.as_view()),
    path("aircraft/<int:pk>/", AircraftReadOnlyViewSet.as_view({"get": "retrieve"})),
    path("aircraft/create/", AircraftCreateAPIView.as_view()),
    path("aircraft/update/<int:pk>", AircraftUpdateAPIView.as_view()),
    path("aircraft/delete/<int:pk>", AircraftDeleteAPIView.as_view()),
]
