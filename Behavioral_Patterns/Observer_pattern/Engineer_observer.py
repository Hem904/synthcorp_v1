from .observer import Observer

class EngineerObserver(Observer):
    def update(self, message):
        print(f"Engineer received update: {message}")

