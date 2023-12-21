from django.urls import path, include
from rest_framework import routers
from .views import AircraftViewSet

router = routers.DefaultRouter()
router.register(r"aircraft", AircraftViewSet)

urlpatterns = [path("", include(router.urls))]
