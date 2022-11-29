from django.urls import path
# from rest_framework.routers import DefaultRouter

from .views import TourCreateView

# router = DefaultRouter()

# # router.register('tour', TourViewSet, 'tour')



urlpatterns = [ 
    path('create-tour/', TourCreateView.as_view(), name='create-tour')
]
# urlpatterns += router.urls