from Creational_Patterns.Factories.Factory_Pattern import MachineFactory
from Creational_Patterns.Central_Control_System.Singleton_patterns import CentralControlSystem
from Creational_Patterns.Builders.Builder_Pattern import ProductionDirector, BudgetLineBuilder, PremiumLineBuilder
from Structural_Pattern.Adapter_pattern.adapter_pattern import MachineAdapter
from Structural_Pattern.Adapter_pattern.Old_machine.old_machine import OldMachine
from Structural_Pattern.Facade.Factory_facade import FactoryFacade
  # Assuming it's saved in FacadePattern.py

def test_factory_facade():
    # Create the factory facade instance
    factory_facade = FactoryFacade()

    print("Starting standard production:")
    factory_facade.start_production()

    print("\nRunning custom production line (Premium):")
    factory_facade.run_custom_line("Premium")

    print("\nRunning custom production line (Budget):")
    factory_facade.run_custom_line("Budget")

if __name__ == "__main__":
    test_factory_facade()
