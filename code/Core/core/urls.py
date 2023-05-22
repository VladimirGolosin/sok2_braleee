from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('parse_and_visualize', views.parse_and_visualize, name="parse_and_visualize")


]