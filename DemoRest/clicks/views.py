from django.shortcuts import render

from rest_framework import generics
from clicks.serializers import *


# Create your views here.
class ClickCreateView(generics.CreateAPIView):
    serializer_class = ClickDetailSerializer
