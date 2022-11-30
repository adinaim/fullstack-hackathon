from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import GuideViewSet, BusinessView, BusinessRetrieveView, BusinessUpdateView, BusinessDeleteView #, BusinessProfileViewSet ,



router = DefaultRouter()

# router.register('business-profile',BusinessProfileViewSet, 'business-profile')
router.register('guide', GuideViewSet, 'guide')




urlpatterns = [ 
    path('business/', BusinessView.as_view(), name='creation'),
    # path('business/<str:slug>/', BusinessView.as_view()),
    path('business/retrieve/<str:slug>/', BusinessRetrieveView.as_view(), name='get_business'),
    path('business/update/<str:slug>/', BusinessUpdateView.as_view(), name='get_business'),
    path('business/delete/<str:slug>/', BusinessDeleteView.as_view(), name='get_business'),
    

    # path('guide/', GuideView.as_view(), name='creation'),
    # path('guide/<str:slug>/', GuideView.as_view()),
]
urlpatterns += router.urls