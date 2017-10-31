# Create your views here.
from rest_framework import viewsets

from sos.models import Sos, Comment
from sos.serializers import SoSSerializer, CommentSerializer


class SosViewSet(viewsets.ModelViewSet):
    queryset = Sos.objects.all()
    serializer_class = SoSSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
