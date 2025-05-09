from abc import ABC, abstractmethod

class ProductionStrategy(ABC):
    @abstractmethod
    def execute_production(self):
        pass

# Concrete Strategy: High Demand Strategy
class HighDemandStrategy(ProductionStrategy):
    def execute_production(self):
        return "Executing high-demand production strategy: Prioritize high production."

# Concrete Strategy: Low Demand Strategy
class LowDemandStrategy(ProductionStrategy):
    def execute_production(self):
        return "Executing low-demand production strategy: Reduce production to conserve resources."

# Concrete Strategy: Resource Efficient Strategy
class ResourceEfficientStrategy(ProductionStrategy):
    def execute_production(self):
        return "Executing resource-efficient production strategy: Optimize resource usage for sustainability."

# Context: Production Strategy Execution
class ProductionContext:
    def __init__(self, strategy: ProductionStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ProductionStrategy):
        self._strategy = strategy

    def execute_production(self):
        return self._strategy.execute_production()
