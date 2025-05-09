from .MachineState import MachineState

class IdleState(MachineState):
    def __init__(self, machine):
        self.machine = machine

    def handle(self, machine):
        print("Machine is currently idle. Switching to active state.")
        from .ActiveState import ActiveState
        machine.set_state(ActiveState(machine))