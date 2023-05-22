from core.model.models import Node, Graph
from core.services.parser import ParserService


class VlafaParser(ParserService):

    def name(self):
        return "Vlafa parser"

    def identifier(self):
        return "dummy_parser_vlafa"

    def parse(self, file):
        joza = Node(nodeName="rxlja", attributes={"bigfoot": True})
        vlada = Node(nodeName="prlina", attributes={"debuje": True, "jede": "klipcinu"})
        bibin = Node(nodeName="xi jinping", attributes={"vraca": "Konstantinopolj", "od": 1999})
        vagner = Node(nodeName="bashar al assad", attributes={"dani_borbe": 123})
        stevan = Node(nodeName="xd", attributes={"lokacija": "bulevar"})
        kajman = Node(nodeName="bro", attributes={"jede": "kfc"})

        edge_matrix = [
            [False, True, True, True, False, False],
            [True, False, True, False, True, True],
            [True, True, False, False, True, False],
            [True, False, False, False, False, False],
            [False, True, True, False, False, False],
            [False, True, False, False, False, False]
        ]

        graf = Graph(nodes=[joza, vlada, bibin, vagner, stevan, kajman], edge_matrix=edge_matrix)
        graf.name = file.name
        return graf
