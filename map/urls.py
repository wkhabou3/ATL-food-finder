from django.urls import path
from . import views

urlpatterns = [
    path('', views.sign_in, name="map"),
]