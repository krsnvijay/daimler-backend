# Create your views here.
# ViewSets define the view behavior.
from django.contrib.auth.models import Group
from oauth2_provider.contrib.rest_framework import IsAuthenticatedOrTokenHasScope, OAuth2Authentication
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from accounts.serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    required_scopes = ['users']
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CurrentUserViewSet(APIView):
    authentication_classes = (TokenAuthentication, OAuth2Authentication)
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    required_scopes = ['users']

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    # permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
