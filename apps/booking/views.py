from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as rest_filter
from rest_framework import filters

from .models import TourPurchase
from .serializers import (
    TourItemsSerializer,
    TourPurchaseSerializer,
    OrderHistorySerializer,
)


class OrderViewSet(ModelViewSet):
    serializer_class = TourPurchaseSerializer
    permission_classes = [IsAuthenticated]   
    filter_backends = [
        filters.SearchFilter, 
        rest_filter.DjangoFilterBackend, 
        filters.OrderingFilter
        ]
    filterset_fields = ['status']
    ordering_fields = ['created_at', 'status']
    search_fields = ['order_id', 'status']

    def get_queryset(self):
        user = self.request.user
        return TourPurchase.objects.filter(user=user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class OrderHistoryView(ListAPIView):
    serializer_class = OrderHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return TourPurchase.objects.filter(user=user)
       