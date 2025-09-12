import numpy as np

# Load data
data = np.genfromtxt("sensor_data.csv", delimiter=",", skip_header=1, usecols=(1,2,3,4))

temperature = data[:,0]
distance    = data[:,1]
battery     = data[:,2]
humidity    = data[:,3]

# Question 1: Stats
print("avg_t:", np.mean(temperature))
print("avg_d:", np.mean(distance))
print("avg_b:", np.mean(battery))
print("avg_h:", np.mean(humidity))

print("min_t:", np.min(temperature))
print("min_d:", np.min(distance))
print("min_b:", np.min(battery))
print("min_h:", np.min(humidity))

print("max_t:", np.max(temperature))
print("max_d:", np.max(distance))
print("max_b:", np.max(battery))
print("max_h:", np.max(humidity))

# Question 2: Highest temperature index
htIndex = np.argmax(temperature)
print("Highest temperature:", temperature[htIndex])

# Question 3: Battery below 30
count = np.sum(battery < 30)
print("Battery below 30:", count)

# Save results to CSV
with open("new_data.csv","w") as d:
    d.write(f"Average temperature: {np.mean(temperature)}\n")
    d.write(f"Min temperature: {np.min(temperature)}\n")
    d.write(f"Max temperature: {np.max(temperature)}\n")
    d.write(f"Battery below 30 count: {count}\n")
