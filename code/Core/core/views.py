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

    if request.method == 'POST':
        selected_parser = request.POST.get('parser')
        selected_visualizer = request.POST.get('visualization')

        parser = None
        parseri = apps.get_app_config('core').plugini_ucitavanje
        for p in parseri:
            if p.name() == selected_parser:
                parser = p
                break

        if parser is not None:
            uploaded_file = request.FILES.get('file')
            graph = parser.parse(uploaded_file)

            add = True
            for g in ucitani_grafovi:
                if g.name == graph.name:
                    add = False

            if add is True:
                ucitani_grafovi.append(graph)

        else:
            print("greska kod parse-ovanja!")

    # Retrieve visualizers and render the template
    context = {"parsers": parseri,"visualizators":viz, "loaded_graphs":ucitani_grafovi,"lmao":"mento miento"}
    return render(request, "index.html", context=context)

def load_and_visualize(request):
    parseri = apps.get_app_config('core').plugini_ucitavanje
    viz = apps.get_app_config('core').plugini_vizualizacija
    ucitani_grafovi = apps.get_app_config('core').ucitani_grafovi

    if request.method == 'POST':
        selected_graph = request.POST.get('graph')
        selected_visualizer = request.POST.get('visualization')

        #itd itd

    context = {"parsers": parseri,"visualizators":viz, "loaded_graphs":ucitani_grafovi, "lmao":"aajajajajaja"}
    return render(request, "index.html", context=context)
