from abc import ABC, abstractmethod

class ProductionLine:
    def __init__(self):
        self.steps = []

    def add_steps (self, step):
        self.steps.append(step)

    def run (self):
        print("Productionline is running")
        for step in self.steps:
            print(f"step: {step}")
        print("Productionline is finished")

#abstract builder class
class productionlinebuilder(ABC):
    @abstractmethod
    def __init__(self):
        self.production_line = ProductionLine()

    @abstractmethod
    def add_lenseshaper(self):
        pass

    @abstractmethod
    def add_nanocoater(self):
        pass

    @abstractmethod
    def add_archipembedder(self):
        pass

    @abstractmethod
    def add_visionclaibrater(self):
        pass

    def get_productionline(self):
        return self.production_line
    
class PremiumLineBuilder(productionlinebuilder):
    def __init__(self):
        self.production_line = ProductionLine()

    def add_lenseshaper(self):
        self.production_line.add_steps("Lenseshaper")

    def add_nanocoater(self):
        self.production_line.add_steps("NanoCoater")

    def add_archipembedder(self):
        self.production_line.add_steps("ARchipEmbedder")

    def add_visionclaibrater(self):
        self.production_line.add_steps("Visionclaibrater")

    def get_productionline(self):
        return self.production_line

    
class BudgetLineBuilder(productionlinebuilder):

    def __init__(self):
        self.production_line = ProductionLine()

    def add_lenseshaper(self):
        self.production_line.add_steps("Lenseshaper")

    def add_nanocoater(self):
        self.production_line.add_steps("NanoCoater")

    def add_archipembedder(self):
        pass

    def add_visionclaibrater(self):
        self.production_line.add_steps("Visionclaibrater")


class ProductionDirector:
    def __init__(self, builder: productionlinebuilder):
        self.builder = builder

    def construct(self):
        self.builder.add_lenseshaper()
        self.builder.add_nanocoater()
        self.builder.add_archipembedder()
        self.builder.add_visionclaibrater()
        return self.builder.get_productionline()