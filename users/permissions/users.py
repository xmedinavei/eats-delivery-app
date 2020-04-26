"""User permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    """Verify that object is the user owner"""

    def has_object_permission(self, request, view, obj):
        """Verify obj and user are the same."""
        return request.user == obj