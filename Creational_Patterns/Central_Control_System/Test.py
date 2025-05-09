from Singleton_patterns import CentralControlSystem
from Factories.Factory_Pattern import LenseshaperMachine,NanoCoaterMachine,ARchipEmbedderMachine,VisionclaibraterMachine

# Get the Singleton instance
control_system = CentralControlSystem()

# Register machines
control_system.register_machine(LenseshaperMachine())
control_system.register_machine(NanoCoaterMachine())
control_system.register_machine(ARchipEmbedderMachine())
control_system.register_machine(VisionclaibraterMachine())

# Start production
control_system.start_production()

# Get logs
logs = control_system.get_logs()
print(logs)

# Stop production
control_system.stop_production()

# Clear logs
control_system.clear_logs()

# Get the system status as a dictionary
status = control_system.to_dict()
print(status)
