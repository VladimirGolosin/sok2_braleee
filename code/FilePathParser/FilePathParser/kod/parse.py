from core.model.models import Node, Graph
from core.services.parser import ParserService
import os
from datetime import datetime
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
            n=0
            for _, dirs, files in os.walk(path):
                n += len(dirs)
                n += len(files)
            for x in os.listdir(filepath):
                curr_path = filepath + "\\" + x
                attributes = {}
                attributes["Size (bytes)"] = os.path.getsize(curr_path)
                attributes["Last modified"] = datetime.fromtimestamp(os.path.getmtime(curr_path)).strftime(
                    '%Y-%m-%d %H:%M:%S')
                attributes["Date created"] = datetime.fromtimestamp(os.path.getctime(curr_path)).strftime(
                    '%Y-%m-%d %H:%M:%S')
                attributes["n"] = n
                node = Node(nodeName=x, attributes=attributes)
                nodes.append(node)
                if os.path.isfile(curr_path):
                    pass
                    # lista.append((x, os.path.getsize(curr_path), filepath.split("\\")[-1]))
                if os.path.isdir(curr_path):
                    func(curr_path)
        func(path)

        graf = Graph(nodes=nodes, edge_matrix=edge_matrix)
        graf.name = file.name
        return graf

