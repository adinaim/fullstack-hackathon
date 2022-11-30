from django.urls import path
# from rest_framework.routers import DefaultRouter

from .views import (
    TourView,
    # TourListView,
    # TourRetrieveView,
    ConcreteTourView,
    ConcreteTourDeleteView,
)

# router = DefaultRouter()

# # router.register('tour', TourViewSet, 'tour')



urlpatterns = [ 
    path('tour/', TourView.as_view(), name='tour'),
    path('tour/<str:slug>/', TourView.as_view(), name='tour'),
    # path('tour-retrive/<str:slug>/', TourRetrieveView.as_view(), name='tour-retrieve')
    path('concrete-tour/', ConcreteTourView.as_view(), name='consrete-tour'),
    path('delete-concrete-tour/', ConcreteTourDeleteView.as_view(), name='delete-concrete-view'),
    path('concrete-tour/<str:slug>/', ConcreteTourView.as_view(), name='consrete-tour'),
]
