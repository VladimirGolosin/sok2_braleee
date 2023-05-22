from core.model.models import Graph
from core.services.visualizator import VisualizatorService
from django.template import Template, Context
import os.path

class SimpleVisualizer(VisualizatorService):
    def name(self):
        return "Simple visualizer"

    def identifier(self):
        return "simple_visualizer"

    def visualize(self, graph:Graph):
        with open(os.path.join(__file__.replace("simplevisualizer.py", ""), 'templates', 'visualizer.html'), 'r') as f:
            rawTemplate = f.read()
        template = Template(rawTemplate)
        context = Context({"graph": graph})
        return template.render(context)