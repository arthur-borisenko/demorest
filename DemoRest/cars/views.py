from django.shortcuts import render
from rest_framework import generics
from cars.serializers import CarListSerializer, CarDetailSerializer
from cars.models import Car


# Create your views here.
class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()

class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
