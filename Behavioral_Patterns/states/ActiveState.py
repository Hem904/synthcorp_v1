from .MachineState import MachineState

class ActiveState(MachineState):
    def __init__(self, machine):
        self.machine = machine

    def handle(self, machine):
        print("Machine is active. Switching to maintenance state.")
        from .MaintenanceState import MaintenanceState
        machine.set_state(MaintenanceState())