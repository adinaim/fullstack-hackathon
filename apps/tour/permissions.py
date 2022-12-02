from rest_framework.permissions import BasePermission
from apps.business.models import BusinessProfile


# class IsOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return request.user.is_authenticated and request.user == obj.user


# class IsCompany(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         # return super().has_object_permission(request, view, obj)
#         user = request.user.is_authenticated and request.user == obj.user
#         # profile = request.company_name.slug
#         if user.company_name.slug:
#             return super().has_object_permission(request, view, obj)


class IsCompany(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and hasattr(request.user, "company")
            # and request.user.member.is_active
            # and request.user.member.is_manager
        )