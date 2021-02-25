from django import forms
from django.db.models import fields
from . models import Recipe, Rating


class RecipeListForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'user':forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'admin', 'type':'hidden'}),
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('recipe', 'stars')