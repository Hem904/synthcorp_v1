from Machines import Machine1
from Behavioral_Patterns.states.IdleState import IdleState

    # Initialize the machine
machine = Machine1("Machine1")

    # Set initial state to Idle
machine.set_state(IdleState())

    # Perform a full cycle of actions through the state transitions
for _ in range(4):  # Assuming 4 states in the loop
    machine.perform_action()

