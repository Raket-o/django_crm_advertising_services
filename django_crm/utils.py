from rest_framework import permissions
from django.contrib.auth.models import User


class HasRolePermission(permissions.BasePermission):
    def __call__(self, *args, **kwargs):
        return self

    def __init__(self, role):
        self.role = role

    def has_permission(self, request, view):
        if request.user.id:

            user = User.objects.get(id=request.user.id)
            groups = set(str(group) for group in user.groups.all())

            if self.role in groups or user.is_staff:
                return True
            else:
                return False

        return False
