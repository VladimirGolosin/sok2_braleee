from core.model.models import Node, Graph
from core.services.parser import ParserService
import os
import json
class JSONParser(ParserService):

    def name(self):
        return "JSON parser"

    def identifier(self):
        return "json_parser"

    def parse(self, file):
        file.open()
        data = json.load(file)

        n = data["n"]
        nodes = []
        node_children = []
        edge_matrix = []
        for i in range(n):
            edge_matrix.append([])
            for j in range(n):
                edge_matrix[i].append(False)
        root = data["root"]
        nodes.append(Node(nodeName=root["name"], attributes=root["attributes"]))
        node_children.append(root["children"])

        i = 0
        while i < len(nodes):
            children = node_children[i]
            for child in children:
                nodes.append(Node(nodeName=child["name"], attributes=child["attributes"]))
                node_children.append(child["children"])
                edge_matrix[i][len(nodes) - 1] = True
                edge_matrix[len(nodes) - 1][i] = True
            i += 1

        file.close()

        graf = Graph(nodes=nodes, edge_matrix=edge_matrix)
        graf.name = file.name
        return graf
