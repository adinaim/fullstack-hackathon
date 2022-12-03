# from django.db import models
# from django.contrib.auth import get_user_model

# from apps.business.models import Guide
# from apps.tour_front.models import Tour



# User = get_user_model()


# RATING_CHOISES = (
#         (1, '1'),
#         (2, '2'),
#         (3, '3'),
#         (4, '4'),
#         (5, '5')
#     )


# class GuideRating(models.Model):
#     user = models.ForeignKey(
#         to=User,
#         on_delete=models.CASCADE,
#         related_name='rating_guide'
#     )
#     guide = models.ForeignKey(
#         to=Guide,
#         on_delete=models.CASCADE
#     )
#     rating = models.CharField(max_length=1, choices=RATING_CHOISES)


# class TourRating(models.Model):
#     user = models.ForeignKey(
#         to=User,
#         on_delete=models.CASCADE,
#         related_name='rating_tour'
#     )
#     tour = models.ForeignKey(
#         to=Tour,
#         on_delete=models.CASCADE
#     )
#     rating = models.CharField(max_length=1, choices=RATING_CHOISES)


# class TourComment(models.Model):
#     user = models.ForeignKey(
#         to=User,
#         on_delete=models.CASCADE,
#         related_name='comment_tour'
#     )
#     tour = models.ForeignKey(
#         to=Tour,
#         on_delete=models.CASCADE
#     )
#     image = models.ImageField(upload_to='media/comment_image', blank=True)
#     comment = models.CharField(max_length=150)


# class TourFavorite(models.Model):
#     user = models.ForeignKey(
#         to=User,
#         on_delete=models.CASCADE,
#         related_name='favorite_tour'
#     )
#     tour = models.ForeignKey(
#         to=Tour,
#         on_delete=models.CASCADE
#     )