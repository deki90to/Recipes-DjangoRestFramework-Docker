from django.db import models, reset_queries
from django.db.models.expressions import OrderBy
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django_resized import ResizedImageField

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

# class User(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name =models.CharField(max_length=20)
#     email = models.EmailField(max_length=30)

#     def __str__(self):
#         return self.first_name, self.last_name, self.email


class Recipe(models.Model):
    user =                  models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name =           models.CharField(max_length=200)
    recipe_ingredients =    models.TextField(max_length=3000)
    recipe_text =           models.TextField(max_length=10000)
    date =                  models.DateTimeField(auto_now_add=True, null=True)
    recipe_image =          ResizedImageField(size=[480, 320], quality=100, upload_to='pictures', blank=True, null=True)
    user_email =            models.EmailField(max_length=50, blank=True)
    # user =                  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.recipe_name} | {self.user}, {self.user_email}')

    class Meta:
        ordering = ['recipe_name']

    def avg_rating(self):
        sum = 0
        ratings = Rate.objects.filter(recipe=self)
        for rating in ratings:
            sum += rating.rate
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 'No Ratings'


# class Ingredients(models.Model):
#     name = models.CharField(max_length=20)
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


# RATE_CHOICES = [
#     (1, 'Very Bad'),
#     (2, 'Bad'),
#     (3, 'Ok'),
#     (4, 'Good'),
#     (5, 'Very Good')
# ]

class Rate(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    # rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    
    def __str__(self):
        return (f'{self.recipe}, {self.rate}')


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)