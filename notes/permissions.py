
from rest_framework import permissions

class IsOwnerOrPublicReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.is_public and request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user



