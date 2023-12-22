from django.urls import path, include
from rest_framework import routers

from available_cities import views

router = routers.SimpleRouter()
router.register(r"cities", views.AvailableCitiesViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
