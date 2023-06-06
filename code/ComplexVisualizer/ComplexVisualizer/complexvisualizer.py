from core.model.models import Graph
from core.services.visualizator import VisualizatorService
from django.template import Template, Context
import os.path

class ComplexVisualizer(VisualizatorService):
    def name(self):
        return "Complex visualizer"

    def identifier(self):
        return "complex_visualizer"

    def visualize(self, graph:Graph):
        with open(os.path.join(__file__.replace("complexvisualizer.py", ""), 'templates', 'visualizer_complex.html'), 'r') as f:
            rawTemplate = f.read()
        template = Template(rawTemplate)
        context = Context({"graph": graph})
        return template.render(context)