from observer import Observer
from observable_machine import ObservableMachine
from Machine import Machine
from Engineer_observer import EngineerObserver
# Create the machine instance (Concrete machine class)
machine = Machine()

# Create an observable machine instance (which will notify observers)
observable_machine = ObservableMachine(machine)

# Create observers (e.g., engineers)
engineer_observer = EngineerObserver()

# Add observer to the observable machine
observable_machine.add_observer(engineer_observer)

# Test product operation
observable_machine.product()
# Should print updates about the machine starting and finishing production

# Test malfunction
observable_machine.malfunction()
# Should print update about the machine malfunctioning

# Test maintenance required
observable_machine.maintenance_required()
# Should print update about the machine requiring maintenance
