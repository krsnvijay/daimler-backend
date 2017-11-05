# Create your views here.

from django_filters import rest_framework as filters
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, IsAuthenticatedOrTokenHasScope
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.parsers import MultiPartParser

from sos.models import Sos, Comment
from sos.serializers import SoSSerializer, CommentSerializer


class SosViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, OAuth2Authentication, SessionAuthentication)
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    queryset = Sos.objects.all()
    serializer_class = SoSSerializer
    parser_classes = (MultiPartParser,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'posted_by', 'level', 'status', 'date')



class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, OAuth2Authentication, SessionAuthentication)
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    queryset = Comment.objects.all()
    parser_classes = (MultiPartParser,)
    serializer_class = CommentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('uid', 'sosid', 'date')
