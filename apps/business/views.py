from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)

from .permissions import IsOwner
from .models import BusinessProfile, Guide
from .serializers import (
    BusinessProfileCreateSerializer,
    BusinessProfileListSerializer,
    BusinessProfileSerializer,
    GuideCreateSerializer,
    GuideSeriaizer,
    GuideListSeriaizer,

)

# class Permissions:
#     def get_permissions(self):
#             if self.action in ['list', 'retrieve']:
#                 self.permission_classes = [AllowAny]
#             if self.action in ['create']:
#                 self.permission_classes = [IsAuthenticated, IsOwner]
#             if self.action in ['destroy']:
#                 self.permission_classes = [IsOwner]#, IsAdminUser]
#             if self.action in ['update', 'partial_update']:
#                 self.permission_classes = [IsOwner]
#             return super().get_permissions()


class BusinessProfileViewSet(ModelViewSet):    # update - запрашивает поле user
    queryset = BusinessProfile.objects.all()
    serializer_class = BusinessProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return BusinessProfileListSerializer
        elif self.action == 'create':
            return BusinessProfileCreateSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated, IsOwner]
        if self.action in ['destroy']:
            self.permission_classes = [IsOwner]#, IsAdminUser]
        if self.action in ['update', 'partial_update']:
            self.permission_classes = [IsOwner]
        return super().get_permissions()





class GuideViewSet(ModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideSeriaizer

    def get_serializer_class(self):
        if self.action == 'list':
            return GuideListSeriaizer
        elif self.action == 'create':
            return GuideCreateSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated, IsOwner]
        if self.action in ['destroy']:
            self.permission_classes = [IsOwner]#, IsAdminUser]
        if self.action in ['update', 'partial_update']:
            self.permission_classes = [IsOwner]
        return super().get_permissions()