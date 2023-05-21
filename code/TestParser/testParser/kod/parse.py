from Core.core.model.models import Node, Graph
from Core.core.services.parser import ParserService


class ParseDummy(ParserService):

    def name(self):
        return "Dummy parser"
        pass

    def identifier(self):
        return "dummy_parser"
        pass

    def parse(self, file_path):

        pass
