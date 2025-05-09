from .Command import Command
class CancelProductionCommand(Command):
    def __init__(self, production_system):
        self._production_system = production_system

    def execute(self):
        self._production_system.cancel_production()

    def undo(self):
        self._production_system.start_production()
