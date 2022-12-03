from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    FavoriteViewSet,
    CommentView,
    RatingView,
    GuideRatingView,
)


router = DefaultRouter()


router.register('tour-favorite', FavoriteViewSet, 'tour-favorite')
router.register('tour-comment', CommentView, 'comment')
router.register('tour-rating', RatingView, 'tour-rating')
router.register('guide-rating', GuideRatingView, 'guide-rating')


urlpatterns = [

]
urlpatterns += router.urls