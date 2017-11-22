from rest_framework import permissions


class IsManagerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # Write permissions are only allowed to the owner of the snippet.
        return request.user.has_perm('critical_list.can_change_status')
