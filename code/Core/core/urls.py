from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('parse_and_visualize', views.parse_and_visualize, name="parse_and_visualize"),
    path('load_and_visualize', views.load_and_visualize, name="load_and_visualize"),
    path('get_data/<str:node_id>', views.get_data, name="get_data"),
    path('search/<str:search_text>/', views.search, name='search'),
    path('filter/<str:filter_text>/', views.filter, name='filter'),

]
