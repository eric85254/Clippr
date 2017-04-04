"""
    This module dictates who is allowed to submit GET, POST, PUT, and DELETE requests to the api views.

    | There are typically two functions:
    |   has_object_permission(self, request, view, obj)
    |   has_permission(self, request, view)

    | The initial defines the authentication necessary to view/modify a particular object of the corresponding model.
    The latter function defines the authentication necessary to view a list of all the objects
    or create a new object (POST)

"""

from rest_framework import permissions

from customer.utils.view_logic import CustomerLogic

'''
    APPOINTMENT PERMISSION
'''


class IsOwnerOfAppointment(permissions.BasePermission):
    """
        Permission for Appointment View - checks for the owner of the appointment.
    """

    def has_object_permission(self, request, view, obj):
        """
            Ensures that only the customer and stylist of an appointment may view or modify the appointment.
        """
        if obj.customer == request.user:
            return True
        elif obj.stylist == request.user:
            return True
        else:
            return False

    def has_permission(self, request, view):
        """
            Ensures that no anonymous user can view or create an appointment.
        """
        if request.user.is_anonymous:
            return False
        else:
            return True


'''
    PORTFOLIO HAIRCUT PERMISSIONS
'''


class IsOwnerOfHaircut(permissions.BasePermission):
    """
        Permission for Haircut View - checks for the owner of the haircut.
    """

    def has_object_permission(self, request, view, obj):
        """
            Returns True if the Stylist is the owner of the haircut.
        """
        if CustomerLogic.is_customer(request) and request.method == 'GET':
            return True

        if obj.stylist == request.user:
            return True
        else:
            return False

    def has_permission(self, request, view):
        """
            Returns True if the user is not anonymous.
        """
        if CustomerLogic.is_customer(request) and request.method != 'GET':
            return False

        if request.user.is_anonymous:
            return False
        else:
            return True


'''
    USER PERMISSIONS
'''


class IsCurrentUserOrSuperUser(permissions.BasePermission):
    """
        Basic User Permissions. You can only view your own User information.
    """

    # General Permissions: Everyone can 'GET' & 'POST'
    # Object Permissions: Users 'GET' 'POST' 'PUT' 'DELETE' their object || Superuser's can access or modify anything

    def has_object_permission(self, request, view, obj):
        """
            Ensures that only User object a current user can view is their own.
            Ensures that super users can view any User object.
        """
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
    """
        Miscellaneous Permissions. Checks to ensure the user is logged in.
    """

    # General Permissions: Only logged in users can 'GET' or 'POST'

    def has_permission(self, request, view):
        """
            Returns true only if the user is not anonymous.
        """
        if request.user.is_anonymous:
            return False
        else:
            return True


class OnlySuperUsersCanModify(permissions.BasePermission):
    """
        Miscellaneous Permissions. Checks to ensure that the user is a super user.
    """

    # General Permissions: Public can 'GET' || Superuser can 'PUT' 'POST' 'DELETE'
    # Object Permissions: General Permissions

    def has_permission(self, request, view):
        """
            No restrictions on GET request. If the request is not a GET, then it may only be submitted by a superuser.
        """
        if request.method == 'GET':
            return True

        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        """
            No restrictions on GET request. If the request is not a GET, then it may only be submitted by a superuser.
        """
        if request.method == 'GET':
            return True

        return request.user.is_superuser