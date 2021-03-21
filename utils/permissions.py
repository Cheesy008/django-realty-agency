from rest_framework.permissions import BasePermission, SAFE_METHODS

from users.models import User
from .enums import UserRole


class RealtyPermission(BasePermission):
    message = 'You do not have permission to manage realty'

    def has_permission(self, request, view):
        user = User.objects.get(id=request.user.id)

        if user.role == UserRole.REALTOR and request.method not in SAFE_METHODS:
            return False

        return True


class IsOwnerOrReadOnly(BasePermission):
    message = 'You can not edit this item'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or \
                User.objects.get(id=request.user.id).role == UserRole.ALL:
            return True

        return obj.created_by == request.user
