from django.urls import path

from .views import (
    FlightReadOnlyAPIView,
    FlightCreateAPIView,
    FlightDeleteAPIView,
    FlightUpdateAPIView,
    FlightExportAPIView,
)

urlpatterns = [
    path("flight/", FlightReadOnlyAPIView.as_view({"get": "list"})),
    path("flight/export/<str:fmt>/", FlightExportAPIView.as_view()),
    path("flight/<int:pk>/", FlightReadOnlyAPIView.as_view({"get": "retrieve"})),
    path("flight/delete/<int:pk>/", FlightDeleteAPIView.as_view()),
    path("flight/update/<int:pk>/", FlightUpdateAPIView.as_view()),
    path("flight/create/", FlightCreateAPIView.as_view()),
]
