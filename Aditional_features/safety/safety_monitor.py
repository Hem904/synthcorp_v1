import logging

class SafetyMonitor:
    def __init__(self, machine):
        self.machine = machine

    def check_hazard(self, condition):
        if condition in ('overheat', 'leakage', 'power_failure', 'hardware_failure'):
            logging.critical(f"[ALERT] {condition} detected! Initiating emergency shutdown.")
            self.emergency_shutdown()

    def emergency_shutdown(self):
        from Behavioral_Patterns.states.ErrorState import ErrorState
        self.machine.set_state(ErrorState(self))

    def alert_operator(self, condition):
        # Imagine a function that sends a critical alert to the operator
        print(f"[ALERT] Operator notified: {condition} detected.")
        logging.info(f"Operator alerted about {condition} issue.")
