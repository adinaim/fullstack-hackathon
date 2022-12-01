from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)
from apps.business.permissions import IsOwner

from .models import Tour
from .serailizers import TourCreateSerializer, TourListSerializer, TourSerializer


class TourViewSet(ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


    def get_serializer_class(self):
        if self.action == 'list':
            return TourListSerializer
        elif self.action == 'create':
            return TourCreateSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list']:
            self.permission_classes = [AllowAny]
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        if self.action in ['destroy']:
            self.permission_classes = [IsOwner, IsAdminUser]
        if self.action in ['update', 'partial_update', 'retrieve']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()