from django.urls import path
from django.views.generic.base import View
from . import views



urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipes'),
    path('add/', views.RecipeCreateView.as_view(), name='add'),
    path('my-recipes/', views.MyRecipeListView.as_view(), name='my-recipes'),
]