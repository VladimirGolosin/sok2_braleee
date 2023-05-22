from abc import abstractmethod, ABC
from core.model.models import Graph


class VisualizatorService(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def identifier(self):
        pass

    @abstractmethod
    def visualize(self, graph:Graph):
        pass