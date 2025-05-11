from abc import ABC, abstractmethod
import psycopg2
from database.db_operations import DB_PARAMS

class Observer(ABC):
    @abstractmethod
    def update(self, machine_name, message):
        pass


class LoggerObserver(Observer):
    def update(self, machine_name, message):
        print(f"[Observer] {machine_name}: {message}")
        
        try:
            conn = psycopg2.connect(**DB_PARAMS)
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO notifications (machine_name, message) VALUES (%s, %s)",
                (machine_name, message)
            )
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            print(f"[Observer Error] Failed to log notification: {e}")
