from abc import abstractmethod, ABC


class ParserService(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def identifier(self):
        pass

    @abstractmethod
    def parse(self, file_path):
        pass