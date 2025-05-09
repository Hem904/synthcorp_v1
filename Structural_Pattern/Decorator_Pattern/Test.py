from Decorator import LenseshaperMachine, NanoCoaterMachine, ARchipEmbedderMachine, VisionclaibraterMachine, RealTimeErrorDetectionDecorator, EnergyEfficientOperationModeDecorator

# Create instances of machines
lenseshaper_machine = LenseshaperMachine()
nanocoater_machine = NanoCoaterMachine()
archip_embedder_machine = ARchipEmbedderMachine()
visionclaibrater_machine = VisionclaibraterMachine()

# Wrap machines with decorators to add additional behaviors
lenseshaper_machine_with_error_detection = RealTimeErrorDetectionDecorator(lenseshaper_machine)
nanocoater_machine_with_energy_mode = EnergyEfficientOperationModeDecorator(nanocoater_machine)

# Call the product() method on the decorated machines
lenseshaper_machine_with_error_detection.product()
nanocoater_machine_with_energy_mode.product()

# You can also decorate machines multiple times
archip_embedder_machine_with_both_decorators = RealTimeErrorDetectionDecorator(EnergyEfficientOperationModeDecorator(archip_embedder_machine))
archip_embedder_machine_with_both_decorators.product()
