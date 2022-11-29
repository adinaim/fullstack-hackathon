from django.urls import path
# from rest_framework.routers import DefaultRouter

from .views import (
    TourView,
    # TourListView,
)

# router = DefaultRouter()

# # router.register('tour', TourViewSet, 'tour')



urlpatterns = [ 
    path('tour/', TourView.as_view(), name='tour'),
    path('tour/<str:slug>/', TourView.as_view(), name='tour'),

    # path('list/', TourListView.as_view(), name='list-tour')
]
# urlpatterns += router.urls