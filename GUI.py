import tkinter as tk
from tkinter import ttk
import requests
import ttkbootstrap as tb
from ttkbootstrap.dialogs import Messagebox
import threading

class SynthCorpApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SynthCorp Control Panel")
        self.root.geometry("1000x600")
        self.style = tb.Style("flatly")  
        self.build_ui()

    def build_ui(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.machine_tab = ttk.Frame(notebook)
        self.production_tab = ttk.Frame(notebook)
        self.inventory_tab = ttk.Frame(notebook)
        self.logs_tab = ttk.Frame(notebook)

        notebook.add(self.machine_tab, text="Machine Control")
        notebook.add(self.production_tab, text="Production")
        notebook.add(self.inventory_tab, text="Inventory")
        notebook.add(self.logs_tab, text="Logs")

        self.build_machine_tab()
        self.build_production_tab()
        self.build_inventory_tab()
        self.build_logs_tab()

    def build_machine_tab(self):
        frame = ttk.LabelFrame(self.machine_tab, text="Machine Management", padding=20)
        frame.pack(fill="x", padx=20, pady=20)

        ttk.Label(frame, text="Machine Name:").grid(row=0, column=0, sticky="w")
        self.machine_name = ttk.Entry(frame, width=30)
        self.machine_name.grid(row=0, column=1, padx=5)

        ttk.Button(frame, text="Register", command=self.register_machine).grid(row=1, column=0, padx=5)
        ttk.Button(frame, text="View State", command=self.view_machine_state).grid(row=1, column=1, padx=5)

    def build_production_tab(self):
        frame = ttk.LabelFrame(self.production_tab, text="Production Control", padding=20)
        frame.pack(fill="x", padx=20, pady=20)

        ttk.Button(frame, text="Start Production", command=self.start_production).pack(side="left", padx=5)
        ttk.Button(frame, text="Pause", command=self.pause_production).pack(side="left", padx=5)
        ttk.Button(frame, text="Cancel", command=self.cancel_production).pack(side="left", padx=5)

        ttk.Label(frame, text="State:").pack(side="left", padx=(20, 5))
        self.machine_state = ttk.Combobox(frame, values=["Idle", "Running", "Paused"])
        self.machine_state.pack(side="left")
        ttk.Button(frame, text="Update State", command=self.update_machine_state).pack(side="left", padx=5)

        # Add dropdown to select production strategy
        ttk.Label(frame, text="Strategy:").pack(side="left", padx=(20, 5))
        self.strategy_choice = ttk.Combobox(frame, values=["High", "Low", "Efficient"])
        self.strategy_choice.pack(side="left")

    def build_inventory_tab(self):
        frame = ttk.LabelFrame(self.inventory_tab, text="Inventory Management", padding=20)
        frame.pack(fill="x", padx=20, pady=20)

        ttk.Label(frame, text="Item:").grid(row=0, column=0)
        self.item_name = ttk.Entry(frame)
        self.item_name.grid(row=0, column=1, padx=5)

        ttk.Label(frame, text="Qty:").grid(row=0, column=2)
        self.item_qty = ttk.Entry(frame)
        self.item_qty.grid(row=0, column=3, padx=5)

        ttk.Button(frame, text="Update Inventory", command=self.update_inventory).grid(row=0, column=4, padx=5)

    def build_logs_tab(self):
        frame = ttk.LabelFrame(self.logs_tab, text="Logs", padding=20)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.logs_box = tk.Text(frame, height=15)
        self.logs_box.pack(fill="both", expand=True)

        ttk.Button(frame, text="Refresh Logs", command=self.fetch_logs).pack(pady=5)

    def register_machine(self):
        name = self.machine_name.get()
        threading.Thread(target=self._register_machine, args=(name,)).start()

    def _register_machine(self, name):
        try:
            response = requests.post("http://localhost:5000/register_machine", json={"name": name})
            if response.status_code == 200:
                self.root.after(0, Messagebox.show_info, "Success", f"Machine '{name}' registered successfully.")
            else:
                self.root.after(0, Messagebox.show_error, "Error", response.json()["message"])
        except Exception as e:
            self.root.after(0, Messagebox.show_error, "Error", f"Exception occurred: {e}")

    def view_machine_state(self):
        name = self.machine_name.get()
        threading.Thread(target=self._view_machine_state, args=(name,)).start()

    def _view_machine_state(self, name):
        try:
            response = requests.get(f"http://localhost:5000/machine_state/{name}")
            if response.status_code == 200:
                state = response.json()
                self.root.after(0, Messagebox.show_info, "Machine State", f"State: {state['current_state']}")
            else:
                self.root.after(0, Messagebox.show_error, "Error", response.json()["message"])
        except Exception as e:
            self.root.after(0, Messagebox.show_error, "Error", f"Exception occurred: {e}")

    def update_machine_state(self):
        name = self.machine_name.get()
        state = self.machine_state.get()
        threading.Thread(target=self._update_machine_state, args=(name, state)).start()

    def _update_machine_state(self, name, state):
        try:
            response = requests.post("http://localhost:5000/update_state", json={"name": name, "state": state})
            if response.status_code == 200:
                self.root.after(0, Messagebox.show_info, "Updated", f"Machine state updated to {state}.")
            else:
                self.root.after(0, Messagebox.show_error, "Error", response.json()["message"])
        except Exception as e:
            self.root.after(0, Messagebox.show_error, "Error", f"Exception occurred: {e}")

    def start_production(self):
        strategy_map = {
            "High": "high_demand",
            "Low": "low_demand",
            "Efficient": "resource_efficient"
        }
        chosen_strategy = strategy_map.get(self.strategy_choice.get(), "high_demand")

        threading.Thread(target=self._start_production, args=(chosen_strategy,)).start()

    def _start_production(self, chosen_strategy):
        try:
            response = requests.post("http://localhost:5000/production", json={
                "action": "startProduction",
                "strategy": chosen_strategy
            })

            if response.status_code == 200:
                self.root.after(0, Messagebox.show_info, "Production Started", response.json().get("message", "Started."))
            else:
                self.root.after(0, Messagebox.show_error, "Error", response.json()["message"])
        except Exception as e:
            self.root.after(0, Messagebox.show_error, "Error", f"Exception occurred: {e}")

    def pause_production(self):
        threading.Thread(target=self._pause_production).start()

    def _pause_production(self):
        try:
            response = requests.post("http://localhost:5000/production", json={"action": "pauseProduction"})
            self._handle_production_response(response)
        except Exception as e:
            self.root.after(0, Messagebox.show_error, "Error", f"Exception occurred: {e}")

    def cancel_production(self):
        threading.Thread(target=self._cancel_production).start()

    def _cancel_production(self):
        try:
            response = requests.post("http://localhost:5000/production", json={"action": "cancelProduction"})
            self._handle_production_response(response)
        except Exception as e:
            self.root.after(0, Messagebox.show_error, "Error", f"Exception occurred: {e}")

    def _handle_production_response(self, response):
        if response.status_code == 200:
            self.root.after(0, Messagebox.show_info, "Success", response.json()["message"])
        else:
            self.root.after(0, Messagebox.show_error, "Error", response.json().get("message", "Unknown error."))

    def update_inventory(self):
        item = self.item_name.get()
        qty = self.item_qty.get()
        threading.Thread(target=self._update_inventory, args=(item, qty)).start()

    def _update_inventory(self, item, qty):
        try:
            response = requests.post("http://localhost:5000/update_inventory", json={"item": item, "quantity": qty})
            if response.status_code == 200:
                self.root.after(0, Messagebox.show_info, "Inventory", f"{item} updated to {qty}.")
            else:
                self.root.after(0, Messagebox.show_error, "Error", response.json()["message"])
        except Exception as e:
            self.root.after(0, Messagebox.show_error, "Error", f"Exception occurred: {e}")

    def fetch_logs(self):
        threading.Thread(target=self._fetch_logs).start()

    def _fetch_logs(self):
        try:
            response = requests.get("http://localhost:5000/logs")
            if response.status_code == 200:
                self.logs_box.delete(1.0, "end")
                self.logs_box.insert("end", "\n".join(response.json()))
            else:
                self.root.after(0, Messagebox.show_error, "Error", "Failed to fetch logs.")
        except Exception as e:
            self.root.after(0, Messagebox.show_error, "Error", f"Exception occurred: {e}")

if __name__ == "__main__":
    root = tb.Window(themename="flatly")
    app = SynthCorpApp(root)
    root.mainloop()
