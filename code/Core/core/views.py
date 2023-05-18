from django.apps.registry import apps
from django.shortcuts import render, redirect


def index(request):
    plugini = apps.get_app_config('core').plugini_ucitavanje
    plugini = plugini.extend(apps.get_app_config('core').plugini_vizualizacija)
    return render(request, "index.html", {"title": "Index", "plugini_ucitavanje": plugini})


def ucitavanje_plugin(request, id):
    # Cuvanje identifikatora plugina na nivou sesije.
    request.session['izabran_plugin_ucitavanje'] = id
    plugini = apps.get_app_config('core').plugini_ucitavanje
    plugini = plugini.extend(apps.get_app_config('core').plugini_vizualizacija)
    # Trazimo plugin sa prosledjenim identifikatorom,
    for i in plugini:
        if i.identifier() == id:
            # te pozivamo funkciju koja podatke upisuje u bazu.
            i.ucitati()
    return redirect('index')


def primer1(request):
    plugini = apps.get_app_config('core').plugini_ucitavanje
    plugini = plugini.extend(apps.get_app_config('core').plugini_vizualizacija)
    return render(request, "primer1.html", {"title": "Primer1", "plugini_ucitavanje": plugini})

