from django.contrib import admin
from django.urls import path, include
from cars.views import CarCreateView,CarListView,CarDetailView


app_name="slimmer"
urlpatterns = [
    path('all/',CarListView.as_view()),
    path("cars/create",CarCreateView.as_view()),
    path("cars/detail/<int:pk>/",CarDetailView.as_view()),
]