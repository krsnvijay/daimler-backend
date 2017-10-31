# Create your views here.
from django_filters import rest_framework as filters
from rest_framework import viewsets

from sos.models import Sos, Comment
from sos.serializers import SoSSerializer, CommentSerializer


class SosViewSet(viewsets.ModelViewSet):
    queryset = Sos.objects.all()
    serializer_class = SoSSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'posted_by', 'level', 'status', 'date')


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('uid', 'sosid', 'date')
