from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)

from .permissions import IsOwner
from .models import BusinessProfile
from .serializers import (
    BusinessProfileCreateSerializer,
    BusinessProfileListSerializer,
    BusinessProfileSerializer,
)



class BusinessProfileViewSet(ModelViewSet):
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
            self.permission_classes = [IsAuthenticated]
        if self.action in ['destroy']:
            self.permission_classes = [IsOwner]#, IsAdminUser]
        if self.action in ['update', 'partial_update']:
            self.permission_classes = [IsOwner]
        return super().get_permissions()