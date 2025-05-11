from database.db_operations import log_production

class CentralControlSystem:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_system()
        return cls._instance

    def _initialize_system(self):
        self.machines = []
        self.logs = []
        self.system_status = "Idle"

   
    def register_machine(self, machine):
        self.machines.append(machine)
        log_message = f"Machine {machine.__class__.__name__} has been successfully added."
        self._log_event(log_message, machine.__class__.__name__)


    def get_machine_names(self):
        return [machine.__class__.__name__ for machine in self.machines]


    def start_production(self):
        self.system_status = "Running"
        self._log_event("Manufacturing process initiated.", "System")

        for machine in self.machines:
            if hasattr(machine, "product") and callable(machine.product):
                result = machine.product()
                self._log_event(result, machine.__class__.__name__)
            else:
                self._log_event("Missing 'product' method.", machine.__class__.__name__)

    def stop_production(self):
        self.system_status = "Paused"
        self._log_event("Manufacturing process halted.", "System")

   
    def _log_event(self, message, machine_name):
        entry = f"[{machine_name}] {message}"
        self.logs.append(entry)
        self._store_log_to_db(machine_name, message)

    def _store_log_to_db(self, machine_name, message):
        log_production(machine_name, message)

    def get_logs(self):
        return self.logs

    def clear_logs(self):
        self.logs = []

    def add_observer_to_all(self, observer):
        for machine in self.machines:
            if hasattr(machine, "add_observer"):
                machine.add_observer(observer)


    # -------------------- Status Summary --------------------

    def to_dict(self):
        return {
            "system_status": self.system_status,
            "machines": self.get_machine_names(),
            "logs": self.logs
        }
