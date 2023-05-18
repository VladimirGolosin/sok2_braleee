from uuid import uuid4


class Node:

    def __init__(self, **kwargs):

        self._id = kwargs.get("id",None)
        self._name = kwargs.get("nodeName", None)
        self._attributes = kwargs.get("attributes", None)


    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def attributes(self):
        return self._attributes

    @attributes.setter
    def attributes(self, value):
        self._attributes = value

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Node):
            return self._id == other.id
        return False

class Graph:

    def __init__(self, **kwargs):
        self._nodes = kwargs.get("nodes", [])
        self._edge_matrix = kwargs.get("edge_matrix", None)

    @property
    def nodes(self):
        return self._nodes

    @nodes.setter
    def nodes(self, value):
        self._nodes = value

    @property
    def edge_matrix(self):
        return self._edge_matrix

    @edge_matrix.setter
    def edge_matrix(self, value):
        self._edge_matrix = value

