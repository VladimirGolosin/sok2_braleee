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
        n = 0
        for _, dirs, files in os.walk(path):
            n += len(dirs)
            n += len(files)
        n+=1
        directory_node = Node(name=path, attributes={
            "Type": "Directory",
            "Size (bytes)": os.path.getsize(path)
        })
        nodes.append(directory_node)
        def func(filepath, parent_index):

            for x in os.listdir(filepath):

                curr_path = os.path.join(filepath, x)
                attributes = {}
                attributes["Size (bytes)"] = os.path.getsize(curr_path)
                attributes["Last modified"] = datetime.fromtimestamp(os.path.getmtime(curr_path)).strftime(
                    '%Y-%m-%d %H:%M:%S')
                attributes["Date created"] = datetime.fromtimestamp(os.path.getctime(curr_path)).strftime(
                    '%Y-%m-%d %H:%M:%S')
                node = Node(nodeName=x, attributes=attributes)
                nodes.append(node)
                matrix_row = []
                matrix_row = [False]*n
                length = len(list(os.listdir(filepath)))
                if os.path.isfile(curr_path):
                    matrix_row[parent_index] = True
                    attributes["Type"] = "File"
                    # lista.append((x, os.path.getsize(curr_path), filepath.split("\\")[-1]))
                if os.path.isdir(curr_path):
                    attributes["Type"] = "Directory"
                    matrix_row[parent_index] = True

                    # matrix_row[parent_index:parent_index + length] = [True] * length
                    func(curr_path, parent_index + length)

                edge_matrix.append(matrix_row[:])
        func(path,0)


        matrix_data = []
        for row in edge_matrix:
            matrix_data.append([int(value) for value in row])

        with open('incidence_matrix.txt', 'w') as file:
            for row in matrix_data:
                file.write(' '.join(str(value) for value in row) + '\n')

        graf = Graph(nodes=nodes, edge_matrix=edge_matrix)
        graf.name = file.name
        return graf

