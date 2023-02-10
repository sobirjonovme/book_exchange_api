from rest_framework.permissions import BasePermission


class IsParticipant(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        user = request.user

        return obj.book1.owner == user or obj.book2.owner == user
