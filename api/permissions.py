from rest_framework import permissions


class IsOwnerOfAppointment(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.customer == request.user:
            return True
        elif obj.stylist == request.user:
            return True
        else:
            return False

class IsOwnerOfHaircut(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.haircut_stylist == request.user:
            return True
        else:
            return False