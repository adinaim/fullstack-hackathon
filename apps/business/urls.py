from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import BusinessProfileViewSet , GuideViewSet, TourViewSet


router = DefaultRouter()

router.register('business-profile',BusinessProfileViewSet, 'business-profile')
router.register('guide', GuideViewSet, 'guide')
router.register('tour', TourViewSet, 'tour')



urlpatterns = [ 

]
urlpatterns += router.urls