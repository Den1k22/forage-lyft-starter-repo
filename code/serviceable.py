
import abc

class Serviceable(abc.ABC):
    @abc.abstractmethod
    def needs_service(self):
        pass