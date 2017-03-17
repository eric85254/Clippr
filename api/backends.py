"""
    Custom backends are specified here.
"""

from rest_framework.authentication import SessionAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
        This backend allows the class based views to not require a CSRF Token when accepting a POST request.
    """

    def enforce_csrf(self, request):
        return
