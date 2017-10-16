from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from app.models import Part
from app.serailizers import PartSerializer


class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
