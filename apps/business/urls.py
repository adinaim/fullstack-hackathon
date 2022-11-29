from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import BusinessProfileViewSet , GuideViewSet, BusinessView, BusinessRetrieveView



router = DefaultRouter()

router.register('business-profile',BusinessProfileViewSet, 'business-profile')
router.register('guide', GuideViewSet, 'guide')




urlpatterns = [ 
    path('business/', BusinessView.as_view(), name='creation'),
    path('business/<str:slug>/', BusinessView.as_view()),
    path('business-retrieve/<str:slug>/', BusinessRetrieveView.as_view(), name='get')
]
urlpatterns += router.urls