from django.urls import path
# from rest_framework.routers import DefaultRouter

from .views import (
    TourView,
    # TourListView,
    TourRetrieveUpdateDeleteView,
    ConcreteTourView,
    ConcreteTourDeleteUpdateView,
)

# router = DefaultRouter()

# # router.register('tour', TourViewSet, 'tour')


urlpatterns = [ 

    path('concrete-tour/<str:slug>/', ConcreteTourDeleteUpdateView.as_view(), name='concrete-tour'),
    path('tour/<str:slug>/', TourRetrieveUpdateDeleteView.as_view(), name='tour-retrieve'),
    path('tour/', TourView.as_view(), name='tour'),
    path('concrete-tour/', ConcreteTourView.as_view(), name='consrete-tour'),
    path('concrete-tour/<str:slug>/', ConcreteTourView.as_view(), name='concrete-tour'),

]
