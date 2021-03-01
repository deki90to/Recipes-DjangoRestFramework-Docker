# from recipes.views import rating
from django import forms
from django.db.models import fields
from . models import Recipe, Rate, RATE_CHOICES


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

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('recipe', 'rate')

    rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)
