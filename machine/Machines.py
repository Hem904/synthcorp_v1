from Behavioral_Patterns.states.IdleState import IdleState
from Behavioral_Patterns.states.ActiveState import ActiveState
from Behavioral_Patterns.states.ErrorState import ErrorState
from Behavioral_Patterns.states.MaintenanceState import MaintenanceState
from database.db_operations import log_production, update_machine_state

class Machine1:
    def __init__(self, name):
        self.name = name
        self.current_state = IdleState(self)
        self.production_started = False  # Track whether production has started
    
    def set_state(self, state):
        self.current_state = state
        state_name = self.current_state.__class__.__name__
        print(f"Machine state changed to {state_name}")
        log_production(self.name, f"State changed to {state_name}")
        update_machine_state(self.name, state_name)
    
    def get_state(self):
        return self.current_state
    
    def perform_action(self):
        if not self.production_started:
            print("[ERROR] Production has not started. You cannot perform any actions.")
            return  # Prevent any actions if production hasn't started
        if self.current_state:
            log_production(self.name, f"Performing action in state {self.current_state.__class__.__name__}")
            self.current_state.handle(self)
        else:
            print("Machine has no state set.")
            log_production(self.name, "Attempted to perform action with no state set.")

    def log_production(self, event):
        print(f"[Machine Log] {event}")

    def add_feature(self, feature):
        print(f"[Feature Added] {feature} added to {self.name}")

    def remove_feature(self, feature):
        print(f"[Feature Removed] {feature} removed from {self.name}")

    def cancel_production(self):
        if not self.production_started:
            print("[ERROR] Cannot cancel production because production has not started.")
            return  # Prevent canceling if production hasn't started
        print(f"[{self.name}] Production canceled.")
        self.set_state(IdleState(self))
        self.production_started = False  # Reset production flag

    def pause_production(self):
        if not self.production_started:
            print("[ERROR] Cannot pause production because production has not started.")
            return  # Prevent pausing if production hasn't started
        print(f"[{self.name}] Production paused.")
        self.set_state(IdleState(self))

    def resume_production(self):
        if not self.production_started:
            print("[ERROR] Cannot resume production because production has not started.")
            return  # Prevent resuming if production hasn't started
        print(f"[{self.name}] Production resumed.")
        self.set_state(ActiveState(self))

    def start_production(self):
        if self.production_started:
            print("[ERROR] Production has already started.")
            return  # Prevent starting production if it’s already started
        print(f"[{self.name}] Production started.")
        self.set_state(ActiveState(self))
        self.production_started = True  # Mark production as started
