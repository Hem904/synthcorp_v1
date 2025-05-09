from flask import Flask, request, jsonify
from database.db_operations import log_production, update_machine_state, get_machine_state, get_logs, update_inventory, get_observer_notifications
from Behavioral_Patterns.Strategy_pattern.production_strategy import ProductionContext, HighDemandStrategy, LowDemandStrategy, ResourceEfficientStrategy
from Aditional_features.safety.safety_monitor import SafetyMonitor
from machine.Machines import Machine1
import psycopg2
from database.db_operations import DB_PARAMS

app = Flask(__name__)

# Register a machine
@app.route("/register_machine", methods=["POST"])
def register_machine():
    data = request.get_json()
    name = data.get("name")
    machine_type = data.get("type", "Generic")

    if not name:
        return jsonify({"status": "error", "message": "Machine name is required"}), 400

    try:
        update_machine_state(name, "Idle")
        log_production(name, "Registered")
        return jsonify({"status": "success", "message": f"Machine '{name}' registered successfully."}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Production Control (Start, Pause, Cancel)
@app.route("/production", methods=["POST"])
def production_control():
    data = request.json
    action = data.get("action")
    strategy_key = data.get("strategy", "high_demand")

    strategies = {
        "high_demand": HighDemandStrategy(),
        "low_demand": LowDemandStrategy(),
        "resource_efficient": ResourceEfficientStrategy()
    }

    if action == "startProduction":
        strategy = strategies.get(strategy_key, HighDemandStrategy())
        context = ProductionContext(strategy)
        message = context.execute_production()
        return jsonify({"status": "success", "message": message})

    elif action == "pauseProduction":
        log_production("Production", "Paused")
        return jsonify({"status": "success", "message": "Production paused."}), 200

    elif action == "cancelProduction":
        log_production("Production", "Cancelled")
        return jsonify({"status": "success", "message": "Production cancelled."}), 200
    
    else:
        return jsonify({"status": "error", "message": "Invalid action."}), 400

# Safety System: Check hazard condition
@app.route("/check_safety", methods=["POST"])
def check_safety():
    data = request.json
    hazard_condition = data.get("condition")

    if not hazard_condition:
        return jsonify({"status": "error", "message": "Condition (e.g. overheat) is required"}), 400

    try:
        safety_monitor = SafetyMonitor(Machine1("Example Machine"))
        safety_monitor.check_hazard(hazard_condition)
        return jsonify({"status": "success", "message": f"Safety check completed for condition: {hazard_condition}."}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Other endpoints (machine state, logs, etc.) remain unchanged...

# View Machine State
@app.route("/machine_state/<machine_name>", methods=["GET"])
def machine_state(machine_name):
    try:
        state = get_machine_state(machine_name)
        if state:
            return jsonify({"name": machine_name, "current_state": state["current_state"], "last_updated": state["last_updated"].isoformat()})
        return jsonify({"message": f"Machine '{machine_name}' not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update Machine State
@app.route("/update_state", methods=["POST"])
def update_state():
    data = request.get_json()
    name = data.get("name")
    state = data.get("state")

    if not name or not state:
        return jsonify({"message": "Machine name and state are required"}), 400

    try:
        update_machine_state(name, state)
        log_production(name, f"State updated to {state}")
        return jsonify({"message": f"Machine '{name}' state updated to {state}."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start, Pause, or Cancel Production
@app.route("/production", methods=["POST"])
def production():
    data = request.get_json()
    action = data.get("action")

    if not action:
        return jsonify({"message": "Action is required (startProduction, pauseProduction, cancelProduction)."}), 400

    try:
        if action == "startProduction":
            # Perform start production logic
            log_production("Production", "Started")
            return jsonify({"message": "Production started."}), 200
        elif action == "pauseProduction":
            # Perform pause production logic
            log_production("Production", "Paused")
            return jsonify({"message": "Production paused."}), 200
        elif action == "cancelProduction":
            # Perform cancel production logic
            log_production("Production", "Cancelled")
            return jsonify({"message": "Production cancelled."}), 200
        else:
            return jsonify({"message": "Invalid action."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get All Logs
@app.route('/logs', methods=['GET'])
def get_logs():
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()
        cur.execute("SELECT timestamp, action FROM production_logs ORDER BY timestamp DESC")
        rows = cur.fetchall()
        cur.close()
        conn.close()

        logs = [f"{row[0]} - {row[1]}" for row in rows]
        return jsonify(logs)
    except Exception as e:
        return jsonify({"error": str(e)}), 500




# Get Logs for Specific Machine
@app.route("/logs/<machine_name>", methods=["GET"])
def logs_for_machine(machine_name):
    try:
        logs = get_logs(machine_name)
        return jsonify([{"machine": row[0], "action": row[1], "timestamp": row[2].isoformat()} for row in logs])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Update Inventory
@app.route("/update_inventory", methods=["POST"])
def update_inventory_route():
    data = request.get_json()
    item = data.get("item")
    quantity = data.get("quantity")

    if not item or not quantity:
        return jsonify({"message": "Item name and quantity are required"}), 400

    try:
        update_inventory(item, quantity)
        return jsonify({"message": f"Inventory for '{item}' updated with quantity {quantity}."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get Observer Notifications
@app.route("/observer_notifications", methods=["GET"])
def observer_notifications():
    try:
        notifications = get_observer_notifications()
        return jsonify(notifications)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
