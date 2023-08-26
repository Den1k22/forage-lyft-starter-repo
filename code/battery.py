import abc

class Battery(abc.ABC):
    @abc.abstractmethod
    def needs_service(self):
        pass