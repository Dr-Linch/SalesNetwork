from rest_framework.permissions import BasePermission


class IsActive(BasePermission):

    def has_permission(self, request, view):
        if request.user.active:
            return True
        else:
            return False
