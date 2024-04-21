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
    # path("register/", RegisterAPI.as_view()),
    # path("login/", LoginAPI.as_view()),
    path("products/", ProductAPI.as_view()),
    # path("customers/", get_customers),
    path("product/<int:product_id>/", get_product),
    path("sentiment/", SentimentAPI.as_view()),
    path("satisfaction/", satisfaction_rate),
    path("customer_count/",customer_count),
    path("total_revenue/", total_revenue),
    path("total_profit/", total_profit),
    # path("products/", prods_by_sentiment) # localhost:8000/api/products?sentiment=NEG sample path
]
