import numpy as np
import matplotlib.pyplot as plt

# Generate weather data for 30 days
days = np.arange(1, 31)

# Max temperature (mean=31°C, std=2)
max_temp = np.random.normal(loc=31, scale=2, size=30)

# Min temperature (5 to 15 degrees less than max temp)
min_temp = max_temp - np.random.uniform(5, 15, size=30)

# Humidity percentage (43% to 92%)
humidity = np.random.uniform(43, 92, size=30)

# Rainfall in mm (mostly dry days, occasional rain)
rainfall = np.random.choice([0, 0, 0, 5, 13, 24], size=30)

# Data Analysis with NumPy
avg_max_temp = np.mean(max_temp)
avg_min_temp = np.mean(min_temp)
max_rainfall = np.max(rainfall)
hottest_day = days[np.argmax(max_temp)]
wettest_day = days[np.argmax(rainfall)]

print(f"Average Max Temperature: {avg_max_temp:.2f} °C")
print(f"Average Min Temperature: {avg_min_temp:.2f} °C")
print(f"Maximum Rainfall: {max_rainfall} mm on Day {wettest_day}")
print(f"Hottest Day: Day {hottest_day} with {max_temp[hottest_day-1]:.2f} °C")

# Step 3: Visualization

# Rainfall as bar chart
plt.figure(figsize=(10,5))
plt.bar(days, rainfall, color='skyblue')
plt.xlabel('Day of Month')
plt.ylabel('Rainfall (mm)')
plt.title('Daily Rainfall')
plt.grid(axis='y')
plt.show()

# Humidity scatter plot vs Max Temperature
plt.figure(figsize=(10,5))
plt.scatter(humidity, max_temp, color='green')
plt.xlabel('Humidity (%)')
plt.ylabel('Max Temperature (°C)')
plt.title('Humidity vs Max Temperature')
plt.grid(True)
plt.show()

# Max and Min temperature over days
plt.figure(figsize=(10,5))
plt.plot(days, max_temp, label='Max Temp (°C)', color='red', marker='o')
plt.plot(days, min_temp, label='Min Temp (°C)', color='blue', marker='o')
plt.xlabel('Day of Month')
plt.ylabel('Temperature (°C)')
plt.title('Daily Max and Min Temperature')
plt.legend()
plt.grid(True)
plt.show()
