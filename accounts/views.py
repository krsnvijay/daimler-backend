# Create your views here.
# ViewSets define the view behavior.
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group
from django.http import Http404
from oauth2_provider.contrib.rest_framework import IsAuthenticatedOrTokenHasScope, OAuth2Authentication
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from accounts.serializers import GroupSerializer, UserSerializer, LogEntrySerializer, PasswordSerializer
from critical_list.models import Part
from critical_list.serailizers import PartSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrTokenHasScope, DjangoModelPermissions]
    required_scopes = ['users']
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrTokenHasScope, DjangoModelPermissions]
    # permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LogEntryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrTokenHasScope, DjangoModelPermissions]
    # permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['users']
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer

class CurrentUserViewSet(APIView):
    authentication_classes = (TokenAuthentication, OAuth2Authentication, SessionAuthentication)
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    required_scopes = ['users']

    def get(self, request):
        return Response(UserSerializer(request.user, context={'request': request}).data)

    def patch(self, request):
        serializer = PasswordSerializer(data=request.data)
        user = request.user
        if serializer.is_valid():
            if not user.check_password(serializer.data.get('old_password')):
                return Response({'detail': 'Old password is incorrect'},
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            user.set_password(serializer.data.get('new_password'))
            user.save()
            return Response({'detail': 'new password set'}, status=status.HTTP_200_OK)

        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class StarredPartsViewSet(APIView):
    authentication_classes = (TokenAuthentication, OAuth2Authentication, SessionAuthentication)
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    required_scopes = ['users']

    def get(self, request):
        return Response(PartSerializer(request.user.starred_parts, context={'request': request}, many=True).data)

    def patch(self, request):
        try:
            request.user.starred_parts.add(Part.objects.get(part_number=request.data['part_number']))
            return Response(PartSerializer(request.user.starred_parts, context={'request': request}, many=True).data)
        except Part.DoesNotExist:
            raise Http404

    def delete(self, request):
        try:
            request.user.starred_parts.remove(Part.objects.get(part_number=request.data['part_number']))
            return Response(PartSerializer(request.user.starred_parts, context={'request': request}, many=True).data)
        except Part.DoesNotExist:
            raise Http404
