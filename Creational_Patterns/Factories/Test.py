from Factory_Pattern import MachineFactory

factory = MachineFactory()
machine = factory.create_machine("nanocoater")
print(machine.product())

machine = factory.create_machine("lenseshaper")
print(machine.product())

machine = factory.create_machine("archipembedder")
print(machine.product())

machine = factory.create_machine("visionclaibrater")
print(machine.product())
