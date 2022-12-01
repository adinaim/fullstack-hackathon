# from rest_framework.urls import path
from rest_framework.routers import DefaultRouter

from .views import TourViewSet

router = DefaultRouter()
router.register('', TourViewSet, 'tour')

urlpatterns = [

]

urlpatterns += router.urls