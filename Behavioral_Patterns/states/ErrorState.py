from .MachineState import MachineState

class ErrorState(MachineState):
    def __init__(self, machine):
        super().__init__()
        self.machine = machine

    def handle(self, machine):
        print("Machine is in error state. Resetting to idle.")
        from .IdleState import IdleState
        machine.set_state(IdleState(machine))      