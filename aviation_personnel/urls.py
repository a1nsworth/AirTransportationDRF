from django.urls import path

from .views import (
    AviationPersonnelUpdateAPIView,
    AviationPersonnelCreateAPIView,
    AviationPersonnelReadOnlyViewSet,
    AviationPersonnelDeleteAPIView,
)

urlpatterns = [
    path("personnel/", AviationPersonnelReadOnlyViewSet.as_view({"get": "list"})),
    path(
        "personnel/<int:pk>/", AviationPersonnelReadOnlyViewSet.as_view({"get": "retrieve"})
    ),
    path("personnel/create/", AviationPersonnelCreateAPIView.as_view()),
    path("personnel/update/<int:pk>/", AviationPersonnelUpdateAPIView.as_view()),
    path("personnel/delete/<int:pk>/", AviationPersonnelDeleteAPIView.as_view()),
]
