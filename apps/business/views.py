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
    GuideListSerializer,
    GuideSerializer,
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


# class BusinessProfileViewSet(ModelViewSet):    # update - запрашивает поле user - put
#     queryset = BusinessProfile.objects.all()
#     serializer_class = BusinessProfileSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

#     def get_serializer_class(self):
#         if self.action == 'list':
#             return BusinessProfileListSerializer
#         elif self.action == 'create':
#             return BusinessProfileCreateSerializer
#         return super().get_serializer_class()

#     def get_permissions(self):
#         if self.action in ['list', 'retrieve']:
#             self.permission_classes = [AllowAny]
#         if self.action in ['create']:
#             self.permission_classes = [IsAuthenticated, IsOwner]
#         if self.action in ['destroy']:
#             self.permission_classes = [IsOwner]#, IsAdminUser]
#         if self.action in ['update', 'partial_update']:
#             self.permission_classes = [IsOwner]
#         return super().get_permissions()


class BusinessView(APIView):

    def get(self, request: Request):
        bus = BusinessProfile.objects.all()
        serializer = BusinessProfileListSerializer(bus, many=True)

        return Response(serializer.data)

    def post(self, request: Request):
        serializer = BusinessProfileCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=self.request.user)
            return Response(
                'Вы успешно создали бизнес-профиль', 
                status=status.HTTP_201_CREATED
            )

    def get_object(self, slug):
        try:
            return BusinessProfile.objects.get(slug=slug)
        except BusinessProfile.DoesNotExist:
            raise Http404

    def put(self, request, slug):   # требует передавать поля
        # user = request.data.get('user')
        # bus = BusinessProfile.objects.get(slug=slug)
        bus = self.get_object(slug)
        serializer = BusinessProfileSerializer(instance=bus, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BusinessRetrieveView(APIView):
    def get(self, request, slug):
        try:
            bus = BusinessProfile.objects.filter(slug=slug)
            serializer = BusinessProfileSerializer(bus, many=True).data
            return Response(serializer)
        except BusinessProfile.DoesNotExist:
            raise Http404


# class BusinessUpdateView(APIView):
#     def get_object(self, pk):
#         try:
#             return BusinessProfile.objects.get(slug=pk)
#         except BusinessProfile.DoesNotExist:
#             raise Http404

    # def put(self, request, pk):
    #     book = self.get_object(pk)
    #     serializer = BookSerilizer(book, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request, pk):   # требует передавать поля
    #     # user = request.data.get('user')
    #     # bus = BusinessProfile.objects.get(slug=slug)
    #     bus = self.get_object(pk)
    #     serializer = BusinessProfileSerializer(instance=bus, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BusinessDeleteView(APIView):
    def delete(self, request: Request, slug):
        # user = request.data.get('user')
        profile = BusinessProfile.objects.get(slug=slug).delete()
        # username = request.user.username
        # User.objects.get(username=username).delete()
        return Response(
            'Ваш бизнес профиль удален.',
            status=status.HTTP_204_NO_CONTENT
        )


class GuideViewSet(ModelViewSet):      # update - user - 
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return GuideListSerializer
        elif self.action == 'create':
            return GuideSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        if self.action in ['create']:
            self.permission_classes = [IsAuthenticated]
        if self.action in ['destroy']:
            self.permission_classes = [IsOwner]#, IsAdminUser]
        if self.action in ['update', 'partial_update']:
            self.permission_classes = [AllowAny] #[IsOwner]
        return super().get_permissions()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


# class GuideView(APIView):
    
#     def get(self, request: Request):
#         guide = Guide.objects.all()
#         serializer = GuideListSerializer(guide, many=True)
#         return Response(serializer.data)

#     def post(self, request: Request):
#         serializer = GuideSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(user=self.request.user)
#             return Response(
#                 'Вы успешно создали гида.', 
#                 status=status.HTTP_201_CREATED
#             )

#     def put(self, request, slug):   # требует передавать поля
#         # user = request.data.get('user')
#         guide = Guide.objects.get(slug=slug)
#         serializer = GuideSerializer(guide, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request: Request, slug):
#         # user = request.data.get('user')
#         guide = Guide.objects.get(slug=slug).delete()
#         # username = request.user.username
#         # User.objects.get(username=username).delete()
#         return Response(
#             'Гид удален из вашего профиля.',
#             status=status.HTTP_204_NO_CONTENT
#         )