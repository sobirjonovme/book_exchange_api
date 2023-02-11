from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsParticipant(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        user = request.user

        return obj.is_participant(user)


class IsSenderOrIsReceiver(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        user = request.user

        return obj.from_user == user or obj.for_book.owner == user


class IsOwnerOrReceiverReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        user = request.user

        if obj.to_user == user and request.method in SAFE_METHODS:
            return True

        return obj.from_user == user
