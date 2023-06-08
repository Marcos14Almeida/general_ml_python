
# Create a Simulated time-series using Monte-Carlo

# =============================================================================
# ================================= Libraries =================================
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
#                                     Main
# =============================================================================

n = 100  # number of time points
x = np.arange(n)
y = 2 * np.sin(x / 10) + np.random.normal(0, 0.5, n)  # add some noise

# Plot the simulated time-series
plt.plot(x, y)
plt.title('Simulated Time-Series')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()

# Perform Monte Carlo simulation on the time-series
num_simulations = 1000
simulated_data = []
for i in range(num_simulations):
    simulated_y = 2 * np.sin(x / 10) + np.random.normal(0, 0.5, n)  # simulate new data with noise
    simulated_data.append(simulated_y)


plt.plot(simulated_data)
plt.title('Simulated Time Series Data')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()

# Plot the distribution of the simulated data
plt.hist(simulated_data[0], bins=20, alpha=0.5, label='Simulated Data')
plt.axvline(y.mean(), color='red', label='Mean of Original Data')
plt.title('Distribution of Simulated Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()
