from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)
from rest_framework import status

from django.contrib.auth import get_user_model

from .serializers import (
    TourCreateSerializer,
    TourListSerializer, 
    TourSerializer,
)
from apps.business.permissions import IsOwner


User = get_user_model()


class TourCreateView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]


    def post(self, request: Request): 
        serializer = TourCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(
                'Тур успешно создан!',
                status=status.HTTP_201_CREATED
            )

    # def get_permissions(self):
    #     # return super().get_permissions()
    #     permission_classes = [IsAuthenticated, IsOwner]