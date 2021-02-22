from django.shortcuts import render
from django.views import generic
from . models import Recipe
from . forms import RecipeListForm, RecipeCreateForm
from django.urls import reverse_lazy

# Create your views here.



class RecipeListView(generic.ListView):
    template_name = 'recipe_list.html'
    model = Recipe
    form_class = RecipeListForm


class RecipeCreateView(generic.CreateView):
    template_name = 'recipe_form.html'
    model = Recipe
    form_class = RecipeCreateForm
    success_url = reverse_lazy('recipes')


class MyRecipeListView(generic.ListView):
    template_name = 'myrecipe_list.html'
    model = Recipe
