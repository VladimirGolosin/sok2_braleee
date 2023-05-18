from django.apps.registry import apps
from django.shortcuts import render


def foce_layout(request):
    plugini = apps.get_app_config('core').plugini_ucitavanje
    prodavnice=[] #spisak svih objekata
    artikli=[] #lel
    return render(request,"primerProdavnicaForceLayout.html",
                  {"title":"Primer prodavnica force layout",
                   "plugini_ucitavanje": plugini,
                   "prodavnice":prodavnice,
                   "artikli":artikli})

def tree_layout(request):
    plugini = apps.get_app_config('core').plugini_ucitavanje
    prodavnice = []  # spisak svih objekata
    artikli = []  # lel
    return render(request,"primerProdavnicaTreeLayout.html",
                  {"title":"Primer prodavnica force layout",
                   "plugini_ucitavanje": plugini,
                   "prodavnice":prodavnice,
                   "artikli":artikli})