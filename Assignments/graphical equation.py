import numpy as np
import matplotlib.pyplot as plt

# Define the function
def equation(x):
    return np.sqrt(1 - (y - 3*np.sqrt(x**2))**2)

# Create the plot
fig, ax = plt.subplots()

# Set the x range
x1 = np.linspace(-5, 0, 1000)
x2 = np.linspace(0, 5, 1000)

# Plot the equation for different values of y
for y in np.linspace(-3, 3, 7):
    ax.plot(x1, equation(x1), label=f"y={y:.2f}")
    ax.plot(x2, equation(x2), label=f"y={y:.2f}")

# Add a legend and labels
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Plot of x^2 + (y - 3√x^2)^2 = 1 in all four quadrants')

# Show the plot
plt.show()
