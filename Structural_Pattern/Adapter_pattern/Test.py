from Old_machine.old_machine import OldMachine
from adapter_pattern import MachineAdapter

# Create an instance of the old machine (legacy system)
old_machine = OldMachine()

# Use the adapter to interact with the old machine through the new interface
adapter = MachineAdapter(old_machine)

# Call the new interface method, which internally calls the old method
print(adapter.product())
