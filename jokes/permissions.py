from rest_framework import permissions
from .models import Riddle


class IsReedPermisions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
    ## faqat o'qiydigonlarga ruxsat beriladi
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user