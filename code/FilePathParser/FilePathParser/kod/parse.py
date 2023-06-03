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
        n = 0
        for _, dirs, files in os.walk(path):
            n += len(dirs)
            n += len(files)
        n+=1
        edge_matrix = [[False] * n for _ in range(n)]
        graf = Graph(nodes=nodes, edge_matrix=edge_matrix)
        graf.name = file.name
        directory_node = Node(nodeName=path, attributes={
            "Type": "Directory",
            "Size (bytes)": os.path.getsize(path)
        })
        #nodes.append(directory_node)
        populate_graph_from_directory(graf, path)

        return graf

def populate_graph_from_directory(graph, directory):
    # Create a node for the current directory
    current_node = Node(nodeName=directory)
    graph.nodes.append(current_node)

    # Traverse the directory recursively
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Create a node for each file and add it to the graph
            file_path = os.path.join(root, file)
            file_node = Node(nodeName=file_path)
            graph.nodes.append(file_node)

            # Add an edge between the file node and the current directory node in the edge matrix
            current_index = graph.nodes.index(current_node)
            file_index = graph.nodes.index(file_node)
            graph.edge_matrix[current_index][file_index] = True

        for subdir in dirs:
            # Recursively populate the graph for each subdirectory
            subdir_path = os.path.join(root, subdir)
            subdir_node = Node(nodeName=subdir_path)
            graph.nodes.append(subdir_node)

            # Add an edge between the subdirectory node and the current directory node in the edge matrix
            current_index = graph.nodes.index(current_node)
            subdir_index = graph.nodes.index(subdir_node)
            graph.edge_matrix[current_index][subdir_index] = True

            # Recursively populate the graph for the subdirectory
            populate_graph_from_directory(graph, subdir_path)

