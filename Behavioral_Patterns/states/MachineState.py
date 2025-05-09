from abc import ABC, abstractmethod

class MachineState(ABC):
    @abstractmethod
    def handle(self, machine):
        pass
