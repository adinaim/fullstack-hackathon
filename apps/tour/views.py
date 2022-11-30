from functools import partial
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)
from rest_framework import status
from slugify import slugify

from django.contrib.auth import get_user_model

from apps.tour.models import Tour, ConcreteTour

from .serializers import (
    TourCreateSerializer,
    TourListSerializer, 
    TourSerializer,
    ConcreteTourSerializer,
    ConcreteTourListSerializer,
    ConcreteTourCreateSerializer,
)
from apps.business.permissions import IsOwner


User = get_user_model()


class TourView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]


    def post(self, request: Request): 
        serializer = TourCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save(user=self.request.user)
            serializer.save()
            return Response(
                'Тур успешно создан!',
                status=status.HTTP_201_CREATED
            )

    def get(self, request: Request):
        # tour = Tour.objects.filter(slug=tour).first()
        tour = Tour.objects.all()
        serializer = TourListSerializer(tour, many=True) 
        return Response(
            serializer.data
        )

    def get_object(self, slug):
        try:
            return Tour.objects.get(slug=slug)
        except Tour.DoesNotExist:
            raise Http404

    def put(self, request, slug):
        tour= self.get_object(slug)
        serializer = TourSerializer(tour, data=request.data)
        if serializer.is_valid():
            # t = Tour.objects.filter(slug=slug).first()
            # t.slug = slugify(tour.title)
            # t.save()
            serializer.save(user=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class TourRetrieveView(APIView):
#     def get(self, request, slug):
#         try:
#             tour = Tour.objects.filter(slug=slug)
#             serializer = TourSerializer(tour, many=True).data
#             return Response(serializer)
#         except Tour.DoesNotExist:
#             raise Http404



class ConcreteTourView(APIView):
    def post(self, request: Request): 
        serializer = ConcreteTourCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                'Тур успешно создан!',
                status=status.HTTP_201_CREATED
            )

    def get(self, request: Request):
        tour = ConcreteTour.objects.all()
        serializer = ConcreteTourListSerializer(tour, many=True) 
        return Response(
            serializer.data
        )

    def get_object(self, slug):
        try:
            return ConcreteTour.objects.get(slug=slug)
        except ConcreteTour.DoesNotExist:
            raise Http404

    def put(self, request, slug):
        tour= self.get_object(slug)
        serializer = ConcreteTourSerializer(tour, data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConcreteTourDeleteView(APIView):
    def destroy(self, request: Request):
        tour = request.tour.title
        ConcreteTour.objects.get(tour=tour).delete()
        return Response(
            'Тур удален!',
            status=status.HTTP_204_NO_CONTENT
        )




# class DeleteAccountView(APIView):
#     permission_classes = [IsAuthenticated]

#     def destroy(self, request: Request):
#         username = request.user.username
#         User.objects.get(username=username).delete()
#         return Response(
#             'Ваш аккаунт удален.',
#             status=status.HTTP_204_NO_CONTENT
#         )