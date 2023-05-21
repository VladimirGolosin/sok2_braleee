import uuid


class Node:

    def __init__(self, **kwargs):

        self._id = uuid.uuid4()
        self._name = kwargs.get("nodeName", None)
        self._attributes = kwargs.get("attributes", None)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def attributes(self):
        return self._attributes

    @name.setter
    def name(self, value: str):
        self._name = value

    @attributes.setter
    def attributes(self, value):
        self._attributes = value

    def __str__(self):
        text = self.name
        for i in self._attributes:
            text += "\n"
            text += text + i
            text += ": " + self._attributes[i]
        return text

    def __eq__(self, other):
        if isinstance(other, Node):
            return self._id == other.id
        return False


class Edge:

    def __init__(self, **kwargs):
        self._id = uuid.uuid4()
        self._first_node = kwargs.get("first_node", None)
        self._second_node = kwargs.get("second_node", None)

    @property
    def id(self):
        return self._id

    @property
    def first_node(self):
        return self._first_node

    @first_node.setter
    def first_node(self, value):
        self._first_node = value

    @property
    def second_node(self):
        return self._second_node

    @second_node.setter
    def second_node(self, value):
        self._first_node = value

    def __str__(self):
        return self._first_node.name + " to " + self._second_node.name

    def __eq__(self, other):
        if isinstance(other, Edge):
            return self._id == other.id
        return False


class Graph:

    def __init__(self, **kwargs):
        self._id = uuid.uuid4()
        self._nodes = kwargs.get("nodes", [])
        self._edges = kwargs.get("edges", [])

    @property
    def nodes(self):
        return self._nodes

    @nodes.setter
    def nodes(self, value):
        self._nodes = value

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, value):
        self._edges = value
