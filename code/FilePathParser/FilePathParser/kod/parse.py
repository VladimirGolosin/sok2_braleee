from core.model.models import Node, Graph
from core.services.parser import ParserService
import os
class FilePathParser(ParserService):

    def name(self):
        return "FilePath parser"

    def identifier(self):
        return "filepath_parser"

    def parse(self, file):
        file.open()
        path = file.readline().decode()
        file.close()

        nodes = []
        edge_matrix = []
        def func(filepath):
            for x in os.listdir(filepath):
                curr_path = filepath + "\\" + x
                if os.path.isfile(curr_path):
                    attributes={}
                    attributes["Size"] = os.path.getsize(curr_path)
                    attributes["Last modified"] = os.path.getmtime(curr_path)
                    attributes["Date created"] = os.path.getctime(curr_path)
                    node = Node(nodeName=x, attributes=attributes)
                    nodes.append(node)
                    # lista.append((x, os.path.getsize(curr_path), filepath.split("\\")[-1]))
                if os.path.isdir(curr_path):
                    # lista.append((x, os.path.getsize(curr_path), filepath.split("\\")[-1]))
                    func(curr_path)
        func(path)

        graf = Graph(nodes=nodes, edge_matrix=edge_matrix)
        graf.name = file.name
        return graf

