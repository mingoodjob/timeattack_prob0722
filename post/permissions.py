from rest_framework.permissions import BasePermission

from user.models import User


class IsCandidateUser(BasePermission):

    def has_permission(self, request, view):
        return request.user.user_type.user_type == "candidate"

