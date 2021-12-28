from django.urls import path
from django.views.generic.edit import UpdateView
from .views import CompanyView
from . import views


urlpatterns = [
    #path('', views.developer, name='developer'),
    path('receipt/', CompanyView.as_view(), name='developer'),
]
