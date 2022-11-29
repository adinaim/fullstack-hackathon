from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import BusinessProfileViewSet , GuideViewSet


router = DefaultRouter()

router.register('business-profile',BusinessProfileViewSet, 'business-profile')
router.register('guide', GuideViewSet, 'guide')




urlpatterns = [ 

]
urlpatterns += router.urls