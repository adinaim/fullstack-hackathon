from rest_framework.urls import path
from rest_framework.routers import DefaultRouter

from .views import OrderViewSet#, OrderHistoryView


router = DefaultRouter()

router.register('order', OrderViewSet, 'orders')
# router.register('history', OrderHistoryView)

urlpatterns = [

]

urlpatterns += router.urls