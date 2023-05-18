from django.urls import path

from core import prodavnica_view

from . import views

for

urlpatterns = [
    path('', views.index, name="index"),
    # Kada korisnik pogodi ovaj endpoint (http://127.0.0.1:8000/ucitavanje/plugin/ucitati_prodavnice_kod),
    # doci ce do ucitavanja plugina, ciji je identifikator "ucitati_prodavnice_kod".
    path('plugin/<str:id>', views.ucitavanje_plugin, name="ucitavanje_plugin"),

]