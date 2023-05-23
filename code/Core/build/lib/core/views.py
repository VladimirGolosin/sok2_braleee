from django.apps.registry import apps
from django.shortcuts import render, redirect


def index(request):
    parseri = apps.get_app_config('core').plugini_ucitavanje
    viz = apps.get_app_config('core').plugini_vizualizacija
    ucitani_grafovi = apps.get_app_config('core').ucitani_grafovi
    context = {"parsers": parseri,"visualizators":viz, "loaded_graphs":ucitani_grafovi}
    return render(request, "index.html", context=context)

from django.http import HttpResponse

def parse_and_visualize(request):
    parseri = apps.get_app_config('core').plugini_ucitavanje
    viz = apps.get_app_config('core').plugini_vizualizacija
    ucitani_grafovi = apps.get_app_config('core').ucitani_grafovi
    trenutni_iscrtan_graf = apps.get_app_config('core').trenutni_iscrtan_graf

    if request.method == 'POST':
        selected_parser = request.POST.get('parser')
        selected_visualizer = request.POST.get('visualization')
        new_graph = None

        parser = None
        for p in parseri:
            if p.name() == selected_parser:
                parser = p
                break

        if parser is not None:
            uploaded_file = request.FILES.get('file')
            new_graph = parser.parse(uploaded_file)

            add = True
            for g in ucitani_grafovi:
                if g.name == new_graph.name:
                    add = False

            if add:
                ucitani_grafovi.append(new_graph)

        else:
            print("greska kod parse-ovanja!")

        visualizer = None
        for v in viz:
            if v.name() == selected_visualizer:
                visualizer = v
                break

        if visualizer is not None:
            trenutni_iscrtan_graf = visualizer.visualize(new_graph)
            print("trenutniiiiiiiii", trenutni_iscrtan_graf)

        else:
            print("greska kod visualizacije!")

    else:
        print("pozvan je get")

    # Retrieve visualizers and render the template
    context = {
        "parsers": parseri,
        "visualizators": viz,
        "loaded_graphs": ucitani_grafovi,
        "rendered_graph": trenutni_iscrtan_graf
    }
    return render(request, "index.html", context=context)


def load_and_visualize(request):
    parseri = apps.get_app_config('core').plugini_ucitavanje
    viz = apps.get_app_config('core').plugini_vizualizacija
    ucitani_grafovi = apps.get_app_config('core').ucitani_grafovi

    if request.method == 'POST':
        selected_graph = request.POST.get('graph')
        selected_visualizer = request.POST.get('visualization')

        #itd itd

    context = {"parsers": parseri,"visualizators":viz, "loaded_graphs":ucitani_grafovi,"rendered_graph":"lmao"}
    return render(request, "index.html", context=context)
