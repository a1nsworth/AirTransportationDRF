from django.urls import path

from .views import (
    ClientUpdateAPIView,
    ClientCreateAPIView,
    ClientDeleteAPIView,
    ClientReadOnlyViewSet,
    ClientExportAPIView,
)

urlpatterns = [
    path("client/", ClientReadOnlyViewSet.as_view({"get": "list"})),
    path("client/export/<str:fmt>/", ClientExportAPIView.as_view()),
    path("client/<int:pk>/", ClientReadOnlyViewSet.as_view({"get": "retrieve"})),
    path("client/create/", ClientCreateAPIView.as_view()),
    path("client/update/<int:pk>/", ClientUpdateAPIView.as_view()),
    path("client/delete/<int:pk>/", ClientDeleteAPIView.as_view()),
]
