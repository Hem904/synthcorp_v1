from .Old_machine.old_machine import OldMachine

class MachineAdapter():
    def __init__(self, old_machine):
        self.old_machine = old_machine

    def product(self):
        return self.old_machine.production()
