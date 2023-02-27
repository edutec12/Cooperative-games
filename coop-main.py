import numpy as np

# Define the satisfaction function for each agent
def agent_satisfaction(price, consumption, comfort):
    return price * (1 - consumption) * comfort

# Define the function to allocate power to each agent
def cooperative_optimization(electric_system, agent_satisfactions):
    total_satisfaction = sum(agent_satisfactions)
    power_allocations = np.zeros(len(agent_satisfactions))
    
    # Allocate power based on each agent's satisfaction function
    for i, satisfaction in enumerate(agent_satisfactions):
        power_allocations[i] = electric_system * (satisfaction / total_satisfaction)
    
    return power_allocations

# Example usage
# Assume the electric system needs 100 units of power
electric_system = 100

# Assume there are four agents with different satisfaction functions
price = [0.5, 0.7, 0.3, 0.6]
consumption = [0.1, 0.3, 0.2, 0.4]
comfort = [0.8, 0.5, 0.6, 0.9]

# Calculate each agent's satisfaction
agent_satisfactions = [agent_satisfaction(price[i], consumption[i], comfort[i]) for i in range(len(price))]

# Allocate power to each agent
power_allocations = cooperative_optimization(electric_system, agent_satisfactions)

# Print the power allocation for each agent
print("Power Allocations: ", power_allocations)
