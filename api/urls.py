from kronos.views import home, product

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", home),
    path("product/", product)
]
