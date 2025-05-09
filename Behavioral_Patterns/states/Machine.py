from IdleState import IdleState
from MachineState import MachineState

class Machine:
    def __init__(self):
        self._state = IdleState(self)  # Initial state is IdleState

    def set_state(self, state: MachineState):
        self._state = state


    def handle(self):
        self._state.handle(self)

