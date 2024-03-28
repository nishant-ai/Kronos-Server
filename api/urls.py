from kronos.views import *

from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register(r"customer", CustomerViewSet, basename="customer")
router.register(r"sale", SaleViewSet, basename="sale")

urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
    path("product/", ProductAPI.as_view()),
    path("sentiment/", SentimentAPI.as_view())
]
