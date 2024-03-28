from kronos.views import *
from dashboard.views import *

from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()

router.register(r"customer", CustomerViewSet, basename="customer")
router.register(r"sale", SaleViewSet, basename="sale")

urlpatterns = router.urls

urlpatterns = [
    path("", include(router.urls)),
    path("product/", ProductAPI.as_view()),
    path("sentiment/", SentimentAPI.as_view()),
    path("satisfaction/", satisfaction_rate),
    path("products/", prods_by_sentiment) # localhost:8000/api/products?sentiment=NEG sample path
]
