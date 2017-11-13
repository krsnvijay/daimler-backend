# Create your views here.
from django.http import Http404
from django_filters import rest_framework as filters
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, IsAuthenticatedOrTokenHasScope
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView

from sos.models import Sos, Comment
from sos.permissions import IsOwnerOrReadOnly, IsManagerOrReadOnly
from sos.serializers import SoSSerializer, CommentSerializer


class SosViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, OAuth2Authentication, SessionAuthentication)
    permission_classes = [IsAuthenticatedOrTokenHasScope, IsOwnerOrReadOnly, DjangoModelPermissions]
    queryset = Sos.objects.all()
    serializer_class = SoSSerializer
    parser_classes = (MultiPartParser,)
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'posted_by', 'level', 'status', 'date')


class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, OAuth2Authentication, SessionAuthentication)
    permission_classes = [IsAuthenticatedOrTokenHasScope, IsOwnerOrReadOnly, DjangoModelPermissions]
    queryset = Comment.objects.all()
    parser_classes = (MultiPartParser,)
    serializer_class = CommentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('posted_by', 'sosid', 'date')


class SosStatusChangeViewSet(APIView):
    authentication_classes = (TokenAuthentication, OAuth2Authentication, SessionAuthentication)
    permission_classes = [IsAuthenticatedOrTokenHasScope, IsManagerOrReadOnly]

    def patch(self, request, pk, format=None):
        try:
            obj = Sos.objects.get(pk=pk)
            serializer = SoSSerializer(obj, data=request.data, context={'request': request}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except Sos.DoesNotExist:
            raise Http404
