from core.model.models import Node, Graph
from core.services.parser import ParserService
class CSVParser(ParserService):

    def name(self):
        return "CSV parser"

    def identifier(self):
        return "csv_parser"

    def parse(self, file):
        file.open()
        n = int(str(file.readline()).split(";")[0][2:])

        nodes = []
        edge_matrix = []
        skip = True
        for line in file:
            id, name, edges, attributes, x = str(line)[2:].split(";")
            if skip is False:
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
            else:
                skip = False
        file.close()

        graf = Graph(nodes=nodes, edge_matrix=edge_matrix)
        graf.name = file.name
        return graf
