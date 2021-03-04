from django.db import models
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.views import generic
from . models import Recipe, Rate
from . forms import RecipeListForm, RecipeCreateForm, RateForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.db.models import Count
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from django.db.models.functions import Length

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


class RateCreateView(generic.CreateView):
    model = Rate
    form_class = RateForm
    template_name = 'rate_form.html'
    success_url = reverse_lazy('recipes')


def details(request, pk):
    recipe_details = Recipe.objects.filter(pk=pk)
    return render(request, 'recipe_details.html', {'recipe_details': recipe_details})


# def rating(request):
    
#     form = RateForm()

#     if request.method == 'POST':
#         print(request.POST)
#         # form = RateForm(request.POST)
         


#     return render(request, 'recipe_list.html', {'form': form})