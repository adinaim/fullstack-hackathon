# from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.generics import ListAPIView
# from django_filters import rest_framework as rest_filter
# from rest_framework import filters
# from rest_framework.generics import CreateAPIView
# from rest_framework.generics import get_object_or_404

# from .models import TourPurchase
# from .serializers import (
#     # TourItemsSerializer,
#     TourPurchaseSerializer,
#     # OrderHistorySerializer,
# )


# class OrderViewSet(ModelViewSet):
#     serializer_class = TourPurchaseSerializer
#     permission_classes = [IsAuthenticated]   

#     def get_queryset(self):
#         user = self.request.user
#         return TourPurchase.objects.filter(user=user)

#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context['request'] = self.request
#         return context


# # class OrderHistoryView(ListAPIView):
# #     serializer_class = OrderHistorySerializer
# #     permission_classes = [IsAuthenticated]

# #     def get_queryset(self):
# #         user = self.request.user
# #         return TourPurchase.objects.filter(user=user)
       

# # class PurchaseCreateView(CreateAPIView):
# #     serializer_class = TourPurchaseSerializer

# #     def get_queryset(self):
# #         user = self.request.user
# #         return TourPurchase.objects.filter(user=user)

# #     def perform_create(self, serializer):
# #         author = get_object_or_404(TourPurchase, id=self.request.data.get('author_id'))
# #         return serializer.save(author=author)

    