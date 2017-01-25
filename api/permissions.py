from rest_framework import permissions


class IsOwnerOfAppointment(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.customer == request.user:
            return True
        elif obj.stylist == request.user:
            return True
        else:
            return False

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        else:
            return True


class IsOwnerOfHaircut(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.haircut_stylist == request.user:
            return True
        else:
            return False

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        elif request.user.is_stylist == 'YES':
            return True
        else:
            return False


class IsCurrentUserOrSuperUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True
        elif request.user.is_superuser:
            return True
        else:
            return False

class IsUserLoggedIn(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        else:
            return True