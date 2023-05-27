from core.model.models import Node, Graph
from core.services.parser import ParserService
class DummyParser(ParserService):

    def name(self):
        return "CSV parser"

    def identifier(self):
        return "csv_parser"

    def parse(self, file):

        joza = Node(nodeName="joza", attributes={"bigfoot":True})
        vlada = Node(nodeName="vlada", attributes={"debuje": True, "jede":"klipcinu"})
        bibin = Node(nodeName="bibin", attributes={"vraca": "Konstantinopolj", "od": 1999})
        vagner = Node(nodeName="vagner", attributes={"dani_borbe": 123})
        stevan = Node(nodeName="stevan", attributes={"lokacija": "bulevar"})
        kajman = Node(nodeName="kajman", attributes={"jede": "kfc"})

        edge_matrix = [
                       [False,True,True,True,False,False],
                       [True,False,True,False,True,True],
                       [True,True,False,False,True,False],
                       [True,False,False,False,False,False],
                       [False,True,True,False,False,False],
                       [False,True,False,False,False,False]
                       ]

        graf = Graph(nodes=[joza,vlada,bibin,vagner,stevan,kajman], edge_matrix=edge_matrix)
        graf.name = file.name
        return graf
