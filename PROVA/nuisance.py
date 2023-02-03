from abc import ABC, abstractmethod

class Nuisance(ABC):
    @abstractmethod
    def annoy(self):
        pass
