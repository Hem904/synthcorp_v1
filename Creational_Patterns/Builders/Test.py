from Builder_Pattern import ProductionDirector, PremiumLineBuilder, BudgetLineBuilder

premium_builder = PremiumLineBuilder()
director = ProductionDirector(premium_builder)

# Construct the production line using the director
premium_line = director.construct()

# Run the premium production line
premium_line.run()

# Create a director for Budget production line
budget_builder = BudgetLineBuilder()
director = ProductionDirector(budget_builder)

# Construct the production line using the director
budget_line = director.construct()

# Run the budget production line
budget_line.run()
