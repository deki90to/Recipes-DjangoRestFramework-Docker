from django.urls import path
from django.views.generic.base import View
from . import views



urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipes'),
    path('add/', views.RecipeCreateView.as_view(), name='add'),
    path('my-recipes/', views.MyRecipeListView.as_view(), name='my-recipes'),
    path('my-recipes/<pk>/delete/', views.MyRecipeDeleteView.as_view(), name='my-recipe-delete'),
    path('my-recipes/<pk>/update/', views.MyRecipeUpdateView.as_view(), name='my-recipe-update'),
    path('search/', views.search, name='search'),


]