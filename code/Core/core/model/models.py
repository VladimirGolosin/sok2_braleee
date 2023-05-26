import uuid


class Node:
    def __init__(self, **kwargs):
        self._id = str(uuid.uuid4())
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

    def getNodeDetails(self):
        details = ""

        # Get the node name
        details += "<b>" + str(self._name) + "</b>" + "<br><br>"

        # Iterate over the node attributes and their values
        for attribute, value in self._attributes.items():
            details += attribute + ": " + str(value) + "<br>"

        return details


class Graph:

    def __init__(self, **kwargs):
        self._id = uuid.uuid4()
        self._nodes = kwargs.get("nodes", [])
        self._name = kwargs.get("nodeName", None)
        self._edge_matrix = kwargs.get("edge_matrix", None)

    @property
    def nodes(self):
        return self._nodes

    @property
    def name(self):
        return self._name

    @nodes.setter
    def nodes(self, value):
        self._nodes = value

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def edge_matrix(self):
        return self._edge_matrix

    @edge_matrix.setter
    def edge_matrix(self, value):
        self._edge_matrix = value

    def __str__(self):
        ime = self.name
        if self._name is None:
            ime = "none"
        text = "ime:" + ime + "\n"
        text += "broj cvorova: " + (str(len(self.nodes)))
        for n in self.nodes:
            text += "\n" + n.name
        return text

    def __eq__(self, other):
        if isinstance(other, Node):
            return self._id == other.id
        return False