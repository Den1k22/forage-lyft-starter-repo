import abc

class Engine(abc.ABC):
    @abc.abstractmethod
    def needs_service(self):
        pass