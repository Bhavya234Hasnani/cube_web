from rest_framework.permissions import BasePermission, SAFE_METHODS

class PublicReadAdminWrite(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
    
class ContactFormPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        return request.user and request.user.is_authenticated
