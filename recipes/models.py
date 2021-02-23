from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=200)
    recipe_ingredients = models.TextField(max_length=3000)
    recipe_text = models.TextField(max_length=10000)
    email = models.EmailField(max_length=50, blank=True)

    def __str__(self):
        return (f'{self.user}, {self.recipe_name} | {self.email}')

    class Meta:
        ordering = ['recipe_name']