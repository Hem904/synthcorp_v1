class ProductionSystem:
    def __init__(self):
        self._is_running = False

    def start_production(self):
        self._is_running = True
        print("Production started")

    def pause_production(self):
        if self._is_running:
            self._is_running = False
            print("Production paused")

    def resume_production(self):
        if not self._is_running:
            self._is_running = True
            print("Production resumed")

    def cancel_production(self):
        self._is_running = False
        print("Production canceled")
