from django.urls import path
from . import views

urlpatterns = [

    path('add/', views.add_restaurant, name='add_restaurant'),
    path('details/', views.restaurant_list, name='restaurant_list'),

]