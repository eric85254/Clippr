from rest_framework import permissions


'''
    APPOINTMENT PERMISSION
'''

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


'''
    PORTFOLIO HAIRCUT PERMISSIONS
'''

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

'''
    USER PERMISSIONS
'''

class IsCurrentUserOrSuperUser(permissions.BasePermission):
    # General Permissions: Everyone can 'GET' & 'POST'
    # Object Permissions: Users 'GET' 'POST' 'PUT' 'DELETE' their object || Superuser's can access or modify anything

    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True
        elif request.user.is_superuser:
            return True
        else:
            return False

'''
    MISCELLANEOUS PERMISSIONS
'''

class IsUserLoggedIn(permissions.BasePermission):
    # General Permissions: Only logged in users can 'GET' or 'POST'

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        else:
            return True


class OnlySuperUsersCanModify(permissions.BasePermission):
    # General Permissions: Public can 'GET' || Superuser can 'PUT' 'POST' 'DELETE'
    # Object Permissions: General Permissions

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True

        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True

        return request.user.is_superuser