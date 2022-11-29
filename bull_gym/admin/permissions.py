from rest_framework.permissions import BasePermission

class AdminUser(BasePermission):
    def has_permission(self, request, view):
        AdminUser.messages = "Necesitas ser admin"
        return request.user.is_superuser or request.user.is_managers