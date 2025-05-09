import logging
class ProductionScheduler:

    def __init__(self, machines):
        self.machines = machines

    def schedule(self):
        logging.info("[Scheduler] Scheduling production tasks...")
        for machine in self.machines:
            if machine.get_state().__class__.__name__ == "IdleState":
                machine.perform_action()
