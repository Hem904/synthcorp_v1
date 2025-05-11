from .observer import Observable

class ObservableMachine(Observable):
    def __init__(self, machine):
        super().__init__()
        self._machine = machine

    def product(self):
        self.notify_observers(f"{self._machine.__class__.__name__} started operation.")

        result = self._machine.product()

        self.notify_observers(f"{self._machine.__class__.__name__} finished operation.")

        return result

    def malfunction(self):
        self.notify_observers(f"{self._machine.__class__.__name__} malfunctioning.")
        self._machine.malfunction()

    def maintenance_required(self):
        self.notify_observers(f"{self._machine.__class__.__name__} requires maintenance.")
        self._machine.maintenance_required()
