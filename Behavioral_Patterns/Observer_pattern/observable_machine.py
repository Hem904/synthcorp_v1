from .observer import Observable
# from Machine import Machine

class ObservableMachine(Observable):
    def __init__(self, machine):
        super().__init__()
        self._machine = machine

    def product(self):
        # Notify observers before machine runs
        self.notify_observers(f"{self._machine.__class__.__name__} started operation.")

        # Run the actual machine's product method
        result = self._machine.product()

        # Notify observers after machine finishes
        self.notify_observers(f"{self._machine.__class__.__name__} finished operation.")

        return result

    def malfunction(self):
        # Notify observers about the malfunction
        self.notify_observers(f"{self._machine.__class__.__name__} malfunctioning.")
        self._machine.malfunction()

    def maintenance_required(self):
        # Notify observers about maintenance requirement
        self.notify_observers(f"{self._machine.__class__.__name__} requires maintenance.")
        self._machine.maintenance_required()
