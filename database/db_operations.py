import psycopg2
from datetime import datetime
from psycopg2 import sql

DB_PARAMS = {
    "dbname": "synthcorp",
    "host": "localhost",
    "port": "5432",
    "user": "postgres",
    "password": "admin"
}

def log_production(machine_name, action):
    """Logs the production action performed on the machine"""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO production_logs (machine_name, action, timestamp) VALUES (%s, %s, %s);",
            (machine_name, action, datetime.now())
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error logging production: {e}")
        raise

def update_machine_state(name, new_state):
    """Updates the state of a machine in the database (Idle, Running, etc.)"""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO machines (name, current_state, last_updated)
            VALUES (%s, %s, %s)
            ON CONFLICT (name) DO UPDATE
            SET current_state = EXCLUDED.current_state,
                last_updated = EXCLUDED.last_updated;
            """,
            (name, new_state, datetime.now())
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error updating machine state: {e}")
        raise

def get_machine_state(name):
    """Fetches the current state of a machine"""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()
        cur.execute("SELECT current_state, last_updated FROM machines WHERE name = %s;", (name,))
        result = cur.fetchone()
        cur.close()
        conn.close()

        if result:
            return {"current_state": result[0], "last_updated": result[1]}
        else:
            return None  # Machine not found
    except Exception as e:
        print(f"Error fetching machine state: {e}")
        raise

def get_logs(machine_name=None):
    """Fetches the logs for all machines or a specific machine"""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()

        if machine_name:
            cur.execute(
                "SELECT action, timestamp FROM production_logs WHERE machine_name = %s ORDER BY timestamp DESC;",
                (machine_name,)
            )
            logs = cur.fetchall()
            result = [
                {"machine": machine_name, "action": row[0], "timestamp": row[1].isoformat()}
                for row in logs
            ]
        else:
            cur.execute(
                "SELECT machine_name, action, timestamp FROM production_logs ORDER BY timestamp DESC;"
            )
            logs = cur.fetchall()
            result = [
                {"machine": row[0], "action": row[1], "timestamp": row[2].isoformat()}
                for row in logs
            ]

        cur.close()
        conn.close()
        return result

    except Exception as e:
        print(f"Error fetching logs: {e}")
        raise


def update_inventory(item, quantity):
    """Updates the inventory in the database"""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO inventory (item_name, quantity)
            VALUES (%s, %s)
            ON CONFLICT (item_name) DO UPDATE
            SET quantity = EXCLUDED.quantity;
            """,
            (item, quantity)
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error updating inventory: {e}")
        raise

def get_observer_notifications():
    """Fetches notifications for the observer system (can be extended)"""
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cur = conn.cursor()
        cur.execute("SELECT message, timestamp FROM notifications ORDER BY timestamp DESC;")
        notifications = cur.fetchall()
        cur.close()
        conn.close()

        return [{"message": row[0], "timestamp": row[1].isoformat()} for row in notifications]
    except Exception as e:
        print(f"Error fetching observer notifications: {e}")
        raise

def store_notification(message):
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute("INSERT INTO notification (message) VALUES (%s)", (message,))
    conn.commit()
    cur.close()
    conn.close()

