from core.model.models import Node, Graph
from core.services.parser import ParserService
class JSONParser(ParserService):

    def name(self):
        return "JSON parser"

    def identifier(self):
        return "json_parser"

    def parse(self, file):
        file.open()
        n = int(str(file.readline()).split(";")[0][2:])

        nodes = []
        edge_matrix = []
        for line in file:
            id, name, edges, attributes, x = str(line)[2:].split(";")
            print(name)
            if name != "Grad":
                node_attributes = {}
                for attribute in attributes.split(","):
                    key, value = attribute.split(":")
                    if str(value).isnumeric():
                        value = int(value)
                    node_attributes[key] = value
                nodes.append(Node(nodeName=name, attributes=node_attributes))
                node_edges = []
                for i in range(1, n + 1):
                    if str(i) in edges.split(","):
                        node_edges.append(True)
                    else:
                        node_edges.append(False)
                edge_matrix.append(node_edges)
        file.close()

        graf = Graph(nodes=nodes, edge_matrix=edge_matrix)
        graf.name = file.name
        return graf
