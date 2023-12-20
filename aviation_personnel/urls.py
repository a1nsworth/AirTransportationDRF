from django.urls import path, include
from rest_framework import routers
from .views import AviationPersonnelViewSet

router = routers.DefaultRouter()
router.register(r"aviation_personnel", AviationPersonnelViewSet)

urlpatterns = [path("", include(router.urls))]
