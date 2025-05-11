class Machine:
    def __init__(self, name):
        self.name = name
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, event):
        for observer in self.observers:
            observer.update(self.name, event)

    def product(self):
        self.notify("Product created")

    def malfunction(self):
        self.notify("Machine malfunctioned")

    def maintenance_required(self):
        self.notify("Maintenance required")
