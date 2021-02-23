from django.shortcuts import render
from django.views import generic
from . models import Recipe
from . forms import RecipeListForm, RecipeCreateForm
from django.urls import reverse_lazy
from django.db.models import Q

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


def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        recipe = Recipe.objects.all().filter(Q(recipe_name__contains=search) | Q(recipe_ingredients__contains=search) | Q(recipe_text__contains=search))
        return render(request, 'search.html', {'recipe': recipe})