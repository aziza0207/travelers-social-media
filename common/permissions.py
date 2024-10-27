from rest_framework import permissions


class IsAuthenticatedNotAdmin(permissions.BasePermission):
    """ Разрешение, которое разрешает доступ только неадминистраторам."""

    def has_permission(self, request, view):
      
        return (
                request.user.is_authenticated
                and not request.user.is_staff
                and not getattr(request.user, 'is_blocked', False)
        )
