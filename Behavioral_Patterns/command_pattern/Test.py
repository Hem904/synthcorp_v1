from ProductionSystem import ProductionSystem
from PauseProductionCommand import PauseProductionCommand

# Initialize the system and control
production_system = ProductionSystem()
pause_command = PauseProductionCommand(production_system)

# Test: Execute pause command and undo it
production_system.start_production()  # Should print "Production started"
pause_command.execute()               # Should print "Production paused"
pause_command.undo()  