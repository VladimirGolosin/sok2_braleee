from django.apps.registry import apps
from django.shortcuts import render, redirect


def index(request):
    parseri = apps.get_app_config('core').plugini_ucitavanje
    viz = apps.get_app_config('core').plugini_vizualizacija
    return render(request, "index.html", {"parsers": parseri,"visualizators":viz})

from django.http import HttpResponse

def parse_and_visualize(request):
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
            print(uploaded_file.name)
            graph = parser.parse(uploaded_file)
            print(graph)

        else:
            print("greska kod parse-ovanja!")

    # Retrieve visualizers and render the template
    viz = apps.get_app_config('core').plugini_vizualizacija
    return render(request, "index.html", {"parsers": parseri, "visualizators": viz})
