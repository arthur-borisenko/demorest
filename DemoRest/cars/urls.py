from django.contrib import admin
from django.urls import path, include
from cars.views import *

app_name="slimmer"
urlpatterns = [
    path("cars/create",CarCreateView.as_view())
]