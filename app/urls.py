from django.urls import include, path
from rest_framework import routers
from .views import OrderViewSet


router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, basename="orders")

urlpatterns = [
    path('', include(router.urls)),
]
