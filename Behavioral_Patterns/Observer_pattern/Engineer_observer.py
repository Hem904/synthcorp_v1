from .observer import Observer

# In your EngineerObserver class
class EngineerObserver(Observer):
    def update(self, message):
        print(f"Engineer received update: {message}")

