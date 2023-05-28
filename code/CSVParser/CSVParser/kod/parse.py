from core.model.models import Node, Graph
from core.services.parser import ParserService
class CSVParser(ParserService):

    def name(self):
        return "CSV parser"

    def identifier(self):
        return "csv_parser"

    def parse(self, file):
        f = open("Files/" + file.name)
        n = int(f.readline().split(";")[0])

        nodes = []
        edge_matrix = []
        for line in f:
            id, name, edges, attributes = line.split(";")
            node_attributes = {}
            for attribute in attributes.split(","):
                key, value = attribute.split(":")
                node_attributes[key] = value
            nodes.append(Node(nodeName=name, attributes=node_attributes))
            node_edges = []
            for i in range(i, n + 1):
                if str(i) in edges.split(","):
                    node_edges.append(True)
                else:
                    node_edges.append(False)
            edge_matrix.append(node_edges)
        f.close()

        graf = Graph(nodes=nodes, edge_matrix=edge_matrix)
        graf.name = file.name
        return graf
