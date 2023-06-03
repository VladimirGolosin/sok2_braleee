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

        n = 0
        for _, dirs, files in os.walk(path):
            n += len(dirs)
            n += len(files)
        n += 1

        nodes = []
        edge_matrix = [[False] * n for _ in range(n)]

        directory_node = makeFileNode(path)
        nodes.append(directory_node)

        def func(parent_node, parent_path):
            children = os.listdir(parent_path)

            for child in children:
                child_path = os.path.join(parent_path, child)
                child_node = makeFileNode(child_path)
                nodes.append(child_node)
                parent_index = nodes.index(parent_node)
                child_index = nodes.index(child_node)
                edge_matrix[parent_index][child_index] = True
                edge_matrix[child_index][parent_index] = True
                if os.path.isdir(child_path):
                    func(child_node, child_path)

        func(directory_node,path)

        graf = Graph(nodes=nodes, edge_matrix=edge_matrix)
        graf.name = file.name
        return graf
def makeFileNode(path):
    attributes={
        "Size (bytes)": os.path.getsize(path),
        "Last modified": datetime.fromtimestamp(os.path.getmtime(path)).strftime(
            '%Y-%m-%d %H:%M:%S'),
        "Date created": datetime.fromtimestamp(os.path.getctime(path)).strftime(
            '%Y-%m-%d %H:%M:%S')
    }
    if(os.path.isdir(path)):
        attributes["Type"]="Directory"
    else:
        attributes["Type"]="File"

    node = Node(nodeName=path.split("\\")[-1], attributes=attributes)
    return node
