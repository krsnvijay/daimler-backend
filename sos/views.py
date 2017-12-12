# Create your views here.
from django_filters import rest_framework as filters
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, IsAuthenticatedOrTokenHasScope
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import DjangoModelPermissions

from sos.models import Comment
from sos.permissions import IsOwnerOrReadOnly
from sos.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, OAuth2Authentication, SessionAuthentication)
    permission_classes = [IsAuthenticatedOrTokenHasScope, IsOwnerOrReadOnly, DjangoModelPermissions]
    queryset = Comment.objects.all()
    parser_classes = (MultiPartParser,)
    serializer_class = CommentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('posted_by', 'date', 'partid', 'userid')
