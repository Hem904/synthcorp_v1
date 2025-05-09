from .MachineState import MachineState

class MaintenanceState(MachineState):
    def handle(self, machine):
        print("Machine is under maintenance. Switching to error state.")
        from .ErrorState import ErrorState
        machine.set_state(ErrorState(machine))
