from django.shortcuts import render

# Create your views here.
from sos.models import Sos
from sos.serializers import SoSSerializer
from rest_framework import viewsets
class SosViewSet(viewsets.ModelViewSet):
    queryset = Sos.objects.all()
    serializer_class = SoSSerializer