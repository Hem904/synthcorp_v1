from Creational_Patterns.Factories.Factory_Pattern import MachineFactory
from Creational_Patterns.Central_Control_System.Singleton_patterns import CentralControlSystem
from Creational_Patterns.Builders.Builder_Pattern import ProductionDirector ,BudgetLineBuilder, PremiumLineBuilder
from Structural_Pattern.Adapter_pattern.adapter_pattern import MachineAdapter
from Structural_Pattern.Adapter_pattern.Old_machine.old_machine import OldMachine
class FactoryFacade:
    def __init__(self):
        self.control_system = CentralControlSystem()
        self.machine = ["Lenseshaper", "NanoCoater", "ARchipEmbedder", "Visionclaibrater"]

    def start_production(self):
        for m in self.machine:
            machine = MachineFactory.create_machine(m)
            self.control_system.register_machine(machine)
            print(machine.product())

        self.control_system.start_production()
        self.control_system.get_logs()
        self.control_system.stop_production()

    def run_custom_line(self, line_type):
        if line_type == "Premium":
            builder = PremiumLineBuilder()
        elif line_type == "Budget":
            builder = BudgetLineBuilder()
        else:
            raise ValueError("broo its not here bro")

        director = ProductionDirector(builder)
        production_line = director.construct()

        print(f"\nRunning {line_type} Production Line:")
        production_line.run()


        my_old_machine = OldMachine()
        adapter = MachineAdapter(my_old_machine)

        control_system = CentralControlSystem()
        control_system.register_machine(adapter)
        print(adapter.product())
