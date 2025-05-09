from .Command import Command
from .ProductionSystem import ProductionSystem

class PauseProductionCommand(Command):
    def __init__(self, production_system):
        self._production_system = production_system

    def execute(self):
        self._production_system.pause_production()

    def undo(self):
        self._production_system.resume_production()