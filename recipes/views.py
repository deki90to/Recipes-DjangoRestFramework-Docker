from django.db import models
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views import generic
from . models import Recipe
from . forms import RecipeListForm, RecipeCreateForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.db.models import Count

# Create your views here.

class RecipeListView(generic.ListView):
    template_name = 'recipe_list.html'
    model = Recipe
    form_class = RecipeListForm
    # context_object_name = 'recipe_list'


class RecipeCreateView(generic.CreateView):
    template_name = 'recipe_form.html'
    model = Recipe
    form_class = RecipeCreateForm
    success_url = reverse_lazy('recipes')


class MyRecipeListView(generic.ListView):
    template_name = 'myrecipe_list.html'
    model = Recipe
    ordering = ['-date']


class MyRecipeDeleteView(generic.DeleteView):
    template_name = 'myrecipe_delete.html'
    model = Recipe
    success_url = reverse_lazy('my-recipes')


class MyRecipeUpdateView(generic.UpdateView):
    template_name = 'myrecipe_update.html'
    model = Recipe
    form_class = RecipeCreateForm
    success_url = reverse_lazy('my-recipes')



def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        recipe = Recipe.objects.all().filter(Q(recipe_name__contains=search) | Q(recipe_ingredients__contains=search) | Q(recipe_text__contains=search))
        return render(request, 'search.html', {'recipe': recipe})
