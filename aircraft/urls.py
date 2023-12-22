from django.urls import path

from .views import (
    AircraftReadOnlyViewSet,
    AircraftUpdateAPIView,
    AircraftCreateAPIView,
    AircraftDeleteAPIView,
)

urlpatterns = [
    path("aircraft/", AircraftReadOnlyViewSet.as_view({"get": "list"})),
    path("aircraft/<int:pk>/", AircraftReadOnlyViewSet.as_view({"get": "retrieve"})),
    path("aircraft/create/", AircraftCreateAPIView.as_view()),
    path("aircraft/update/<int:pk>", AircraftUpdateAPIView.as_view()),
    path("aircraft/delete/<int:pk>", AircraftDeleteAPIView.as_view()),
]
