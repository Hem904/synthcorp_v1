from database.db_operations import log_production, update_machine_state
from Behavioral_Patterns.states.IdleState import IdleState
from Behavioral_Patterns.states.ActiveState import ActiveState
from Behavioral_Patterns.command_pattern.PauseProductionCommand import PauseProductionCommand
from Behavioral_Patterns.command_pattern.CancelProductionCommand import CancelProductionCommand
from Behavioral_Patterns.command_pattern.ProductionSystem import ProductionSystem
from Behavioral_Patterns.command_pattern.ProductionControl import ProductionControl
from Behavioral_Patterns.Strategy_pattern.production_strategy import HighDemandStrategy, LowDemandStrategy, ResourceEfficientStrategy
from machine.Machines import Machine1
from Aditional_features.safety.safety_monitor import SafetyMonitor
from Aditional_features.inventory.inventory_manager import InventoryManager

def main():
    # Initialize core components
    production_system = ProductionSystem()
    production_control = ProductionControl()
    safety_monitor = SafetyMonitor(None)  # Will assign to the correct machine later
    inventory_manager = InventoryManager()

    # Initialize strategy pattern
    high_demand_strategy = HighDemandStrategy()
    low_demand_strategy = LowDemandStrategy()
    resource_efficient_strategy = ResourceEfficientStrategy()

    # List to store registered machines
    registered_machines = []
    current_machine = None  # To store the currently selected machine

    while True:
        print("\n--- Manufacturing System CLI ---")
        print("1. Register a New Machine")
        print("2. Start Production")
        print("3. Pause Production")
        print("4. Resume Production")
        print("5. Cancel Production")
        print("6. View Current Machine Status")
        print("7. Update Inventory")
        print("8. Check Safety (Overheat/Leakage)")
        print("9. Change Production Strategy")
        print("10. Exit")

        choice = input("Select an action by number: ")

        if choice == "1":
            # Register a new machine
            machine_name = input("Enter machine name: ")
            machine = Machine1(machine_name)
            registered_machines.append(machine)
            safety_monitor.machine = machine  # Link safety monitor to the newly registered machine
            print(f"Machine '{machine_name}' registered successfully.")

        elif choice == "2":
            # Select a machine to start production
            if not registered_machines:
                print("No machines registered yet. Please register a machine first.")
                continue
            print("Select a machine to start production:")
            for i, machine in enumerate(registered_machines, start=1):
                print(f"{i}. {machine.name}")
            machine_choice = int(input("Choose a machine: ")) - 1
            if 0 <= machine_choice < len(registered_machines):
                selected_machine = registered_machines[machine_choice]
                selected_machine.start_production()
                print(f"Production started for {selected_machine.name}.")
                current_machine = selected_machine  # Set the current machine
            else:
                print("Invalid machine choice.")

        elif choice == "3":
            # Pause production for selected machine
            if not registered_machines or current_machine is None:
                print("No active machine selected. Please start production first.")
                continue
            current_machine.pause_production()
            print(f"Production paused for {current_machine.name}.")

        elif choice == "4":
            # Resume production for selected machine
            if not registered_machines or current_machine is None:
                print("No active machine selected. Please start production first.")
                continue
            current_machine.resume_production()
            print(f"Production resumed for {current_machine.name}.")

        elif choice == "5":
            # Cancel production for selected machine
            if not registered_machines or current_machine is None:
                print("No active machine selected. Please start production first.")
                continue
            current_machine.cancel_production()
            print(f"Production canceled for {current_machine.name}.")


        elif choice == "6":
            # View current machine status
            if not registered_machines or current_machine is None:
                print("No active machine selected. Please start production first.")
                continue
            print(f"Current machine status for {current_machine.name}: {current_machine.get_state().__class__.__name__}")

        elif choice == "7":
            # Update inventory
            item = input("Enter material name to update (e.g., lens_material): ")
            quantity = int(input("Enter quantity to update: "))
            inventory_manager.update_inventory(item, quantity)
            print(f"Updated inventory for {item}: {quantity} units.")

        elif choice == "8":
            # Check safety
            condition = input("Enter condition for safety check (overheat, leakage): ")
            safety_monitor.check_hazard(condition)
            print(f"Safety check performed for condition: {condition}")

        elif choice == "9":
            # Change production strategy
            if not registered_machines or current_machine is None:
                print("No active machine selected. Please start production first.")
                continue
            print("\nAvailable Strategies:")
            print("1. High Demand Strategy")
            print("2. Low Demand Strategy")
            print("3. Resource Efficient Strategy")
            strategy_choice = input("Select a strategy by number: ")

            if strategy_choice == "1":
                print(high_demand_strategy.execute_production())
            elif strategy_choice == "2":
                print(low_demand_strategy.execute_production())
            elif strategy_choice == "3":
                print(resource_efficient_strategy.execute_production())
            else:
                print("Invalid strategy choice.")

        elif choice == "10":
            # Exit the program
            print("Exiting the system.")
            break  # Exit the loop and end the program

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
