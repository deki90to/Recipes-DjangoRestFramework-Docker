from django.conf import settings
from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=200)
    recipe_ingredients = models.TextField(max_length=3000)
    recipe_text = models.TextField(max_length=10000)
    email = models.EmailField(max_length=50, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return (f'{self.user}, {self.recipe_name} | {self.email}')

    class Meta:
        ordering = ['recipe_name']

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(recipe=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0



class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return (f'{self.recipe}, {self.stars}')

