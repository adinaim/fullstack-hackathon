from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import BusinessProfileViewSet


router = DefaultRouter()

router.register('',BusinessProfileViewSet, 'business-profile')

urlpatterns = [ 

]
urlpatterns += router.urls