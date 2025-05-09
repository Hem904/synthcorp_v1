from production_strategy import HighDemandStrategy, LowDemandStrategy, ResourceEfficientStrategy, ProductionContext

# Create the context with the initial strategy
production_context = ProductionContext(HighDemandStrategy())

# Execute production with the initial strategy (High Demand)
print(production_context.execute_production())

# Change the strategy to Low Demand
production_context.set_strategy(LowDemandStrategy())
print(production_context.execute_production())

# Change the strategy to Resource Efficient
production_context.set_strategy(ResourceEfficientStrategy())
print(production_context.execute_production())
