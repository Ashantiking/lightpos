
from django.urls import path
from django.views.generic.edit import UpdateView
from .views import CategoryView
urlpatterns = [
    path('', CategoryView.as_view(), name='category'),
    ]