from django.urls import path
from django.urls.resolvers import URLPattern
from . views import Register

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
]