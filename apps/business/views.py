from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)
from django.http import Http404

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


class BusinessProfileViewSet(ModelViewSet):    # update - запрашивает поле user - put
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


class BusinessView(APIView):

    def post(self, request: Request):
        serializer = BusinessProfileCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=self.request.user)
            return Response(
                'Вы успешно создали бизнес-профиль', 
                status=status.HTTP_201_CREATED
            )

    def get(self, request: Request):
        bus = BusinessProfile.objects.all()
        serializer = BusinessProfileListSerializer(bus, many=True)

        return Response(serializer.data)

    def get_object(self, pk):    # permissison - for 
        try:
            return BusinessProfile.objects.get(slug=pk)
        except BusinessProfile.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        bus = self.get_object(pk)
        serializer = BusinessProfileSerializer(bus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    # def patch():
    #     ...

    # def destroy():
    #     ...


class BusinessRetrieveView(APIView):
    def get(self, request, slug):
        try:
            bus = BusinessProfile.objects.filter(slug=slug)
            serializer = BusinessProfileSerializer(bus, many=True).data
            return Response(serializer)
        except BusinessProfile.DoesNotExist:
            raise Http404





class GuideViewSet(ModelViewSet):      # update - user - 
    queryset = Guide.objects.all()
    serializer_class = GuideSeriaizer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

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