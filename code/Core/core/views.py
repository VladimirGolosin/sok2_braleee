import uuid

from django.apps.registry import apps
from django.shortcuts import render
from django.http import JsonResponse
from core.model.models import Node, Graph

def index(request):
    parseri = apps.get_app_config('core').plugini_ucitavanje
    viz = apps.get_app_config('core').plugini_vizualizacija
    ucitani_grafovi = apps.get_app_config('core').ucitani_grafovi
    context = {"parsers": parseri,"visualizators":viz, "loaded_graphs":ucitani_grafovi}
    return render(request, "index.html", context=context)

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
                apps.get_app_config('core').trenutni_vizualizator = v
                break

        if visualizer is not None:
            trenutni_iscrtan_graf = visualizer.visualize(new_graph)
            #obavestiti core pošto ovo nije lista
            apps.get_app_config('core').trenutni_iscrtan_graf = trenutni_iscrtan_graf
            apps.get_app_config('core').trenutni_graf = new_graph

        else:
            print("greska kod visualizacije!")

    else:
        print("pozvan je get")
    
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
    trenutni_iscrtan_graf = apps.get_app_config('core').trenutni_iscrtan_graf

    if request.method == 'POST':
        selected_graph = request.POST.get('graph')
        selected_visualizer = request.POST.get('visualization')

        print("selektovaniii", selected_graph)
        graph_to_display = None
        for g in ucitani_grafovi:
            if g.name == selected_graph:
                graph_to_display = g
                print("nasao sam grafff",graph_to_display)
                break

        visualizer = None
        for v in viz:
            if v.name() == selected_visualizer:
                visualizer = v
                apps.get_app_config('core').trenutni_vizualizator = v
                break

        if visualizer and graph_to_display:
            trenutni_iscrtan_graf = visualizer.visualize(graph_to_display)
            # obavestiti core pošto ovo nije lista
            apps.get_app_config('core').trenutni_iscrtan_graf = trenutni_iscrtan_graf
            apps.get_app_config('core').trenutni_graf = graph_to_display

        else:
            print("greska kod visualizacije!")

    else:
        print("pozvan je get")

    context = {
        "parsers": parseri,
        "visualizators": viz,
        "loaded_graphs": ucitani_grafovi,
        "rendered_graph": trenutni_iscrtan_graf
    }
    return render(request, "index.html", context=context)



def get_data(request, node_id):
    text = "xd"

    print(apps.get_app_config('core').trenutni_graf.nodes)
    for n in apps.get_app_config('core').trenutni_graf.nodes:
        if n.id == node_id:
            text = n.getNodeDetails()  # Corrected method name

    data = {
        'message': text,
    }

    return JsonResponse(data)


def search_graph(graph, search_text):
    new_graph = Graph(nodes=[], name=graph.name)
    node_mapping = {}

    for index, node in enumerate(graph.nodes):
        found = False
        if search_text in str(node):
            found = True
        else:
            for value in node.attributes.values():
                if search_text in str(value):
                    found = True
                    break

        if found:
            new_graph.nodes.append(node)
            node_mapping[index] = len(new_graph.nodes) - 1

    new_edge_matrix = []
    for _ in range(len(new_graph.nodes)):
        new_edge_matrix.append([False] * len(new_graph.nodes))

    for i in range(len(graph.nodes)):
        for j in range(len(graph.nodes)):
            if i in node_mapping and j in node_mapping:
                new_i = node_mapping[i]
                new_j = node_mapping[j]
                new_edge_matrix[new_i][new_j] = graph.edge_matrix[i][j]

    new_graph.edge_matrix = new_edge_matrix
    return new_graph




def search(request, search_text):
    viz = apps.get_app_config('core').trenutni_vizualizator
    pretrazen_graf = search_graph(apps.get_app_config('core').trenutni_graf, search_text)
    trenutni_iscrtan_graf = viz.visualize(pretrazen_graf)
    # obavestiti core pošto ovo nije lista
    apps.get_app_config('core').trenutni_iscrtan_graf = trenutni_iscrtan_graf
    apps.get_app_config('core').trenutni_graf = pretrazen_graf

    context = {
        "parsers": apps.get_app_config('core').plugini_ucitavanje,
        "visualizators": apps.get_app_config('core').plugini_vizualizacija,
        "loaded_graphs": apps.get_app_config('core').ucitani_grafovi,
        "rendered_graph": apps.get_app_config('core').trenutni_iscrtan_graf,
        "search_filter_current_text": search_text,
    }
    return render(request, "index.html", context=context)


def filter(request, filter_text):
    viz = apps.get_app_config('core').trenutni_vizualizator
    filtriran_graf = search_graph(apps.get_app_config('core').trenutni_graf, filter_text)
    trenutni_iscrtan_graf = viz.visualize(filtriran_graf)
    # obavestiti core pošto ovo nije lista
    apps.get_app_config('core').trenutni_iscrtan_graf = trenutni_iscrtan_graf
    apps.get_app_config('core').trenutni_graf = filtriran_graf

    context = {
        "parsers": apps.get_app_config('core').plugini_ucitavanje,
        "visualizators": apps.get_app_config('core').plugini_vizualizacija,
        "loaded_graphs": apps.get_app_config('core').ucitani_grafovi,
        "rendered_graph": apps.get_app_config('core').trenutni_iscrtan_graf,
        "search_filter_current_text": filter_text,
    }
    return render(request, "index.html", context=context)
