from core.model.models import Node, Graph
from core.services.parser import ParserService
class DummyParser(ParserService):

    def name(self):
        return "Dummy parser"

    def identifier(self):
        return "dummy_parser"

    def parse(self, file):

        joza = Node(nodeName="joza", attributes={"bigfoot":True, "visina":187, "lokacija":"kikinda"})
        vlada = Node(nodeName="vlada", attributes={"debuje": True, "jede":"klipcinu", "visina":172, "lokacija":"livade"})
        bibin = Node(nodeName="bibin", attributes={"vraca": "Konstantinopolj", "od": 1999, "visina":187,"lokacija":"livade"})
        vagner = Node(nodeName="vagner", attributes={"dani_borbe": 123, "visina":177,"lokacija":"bahmut"})
        stevan = Node(nodeName="stevan", attributes={"lokacija": "bulevar", "visina":190,})
        kajman = Node(nodeName="kajman", attributes={"jede": "kfc", "visina":200,"lokacija":"zimbabve"})

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
