from django.urls import path, include
from rest_framework import routers

from available_cities.views import AvailableCitiesViewSet, AvailableCitiesExportAPIView

router = routers.SimpleRouter()
router.register(r"cities", AvailableCitiesViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("cities/export/<str:fmt>/", AvailableCitiesExportAPIView.as_view()),
]
