import numpy as np
import random

def generate_data_stream(size=1000, seasonality=50):
    """Simulates a data stream with noise and seasonality."""
    stream = []
    for i in range(size):
        # Generate a seasonal pattern (e.g., sine wave)
        seasonal = np.sin(i / seasonality) * 10
        
        # Add some random noise
        noise = random.uniform(-2, 2)
        
        # Create a normal data point
        value = seasonal + noise
        stream.append(value)
    
    return stream

# Example of data stream
data_stream = generate_data_stream()


def detect_anomalies(data, threshold=3):
    """Detects anomalies in the data stream using z-score."""
    if len(data) == 0:
        raise ValueError("Data stream is empty")
    
    mean = np.mean(data)
    std_dev = np.std(data)
    if std_dev == 0:
        raise ValueError("Standard deviation is zero, no variation in data.")
    
    anomalies = []
    for i, value in enumerate(data):
        z_score = (value - mean) / std_dev
        if np.abs(z_score) > threshold:
            anomalies.append((i, value))  # Store index and value of the anomaly
            
    return anomalies


# Detect anomalies in the stream
anomalies = detect_anomalies(data_stream)
print(f"Anomalies found: {anomalies}")


from collections import deque

def real_time_anomaly_detection(window_size=100, threshold=3):
    """Detect anomalies in real-time with a sliding window."""
    window = deque(maxlen=window_size)  # Store a fixed-size window of data points
    
    for i, value in enumerate(data_stream):
        window.append(value)
        
        # Only start detecting anomalies when the window is full
        if len(window) == window_size:
            mean = np.mean(window)
            std_dev = np.std(window)
            z_score = (value - mean) / std_dev
            
            if np.abs(z_score) > threshold:
                print(f"Anomaly detected at index {i}: {value}")

# Simulate real-time anomaly detection
real_time_anomaly_detection()


import matplotlib.pyplot as plt

def plot_data_with_anomalies(data, anomalies):
    plt.plot(data, label="Data Stream")
    
    # Highlight anomalies in red
    for index, value in anomalies:
        plt.scatter(index, value, color='red', label="Anomaly" if index == anomalies[0][0] else "")
    
    plt.title("Real-Time Data Stream with Anomalies")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend()
    plt.show()

# Plot the data and anomalies
plot_data_with_anomalies(data_stream, anomalies)
