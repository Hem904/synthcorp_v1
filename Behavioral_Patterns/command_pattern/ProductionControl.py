from .Command import Command
class ProductionControl:
    def __init__(self):
        self._command_history = []

    def execute_command(self, command: Command):
        command.execute()
        self._command_history.append(command)

    def undo_last_command(self):
        if self._command_history:
            last_command = self._command_history.pop()
            last_command.undo()
