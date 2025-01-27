from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission untuk memastikan hanya pemilik atau admin yang dapat
    mengakses/mengubah data.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions diberikan untuk request GET
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions hanya untuk pemilik atau admin
        return obj.member == request.user or request.user.role == 'admin'

class IsAdminUser(permissions.BasePermission):
    """
    Permission untuk membatasi akses hanya untuk admin.
    """
    def has_permission(self, request, view):
        return request.user and request.user.role == 'admin' 