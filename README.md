# DataStreamProject
Efficient Data Stream Anomaly Detection

Project Overview
The Efficient Data Stream Anomaly Detection project is a Python script designed to detect anomalies in real-time within a continuous data stream. This stream mimics real-world data such as financial transactions or system metrics, combining regular patterns, random noise, and seasonal variations. The script utilizes a statistical z-score method to flag unusual data points and offers real-time visualization to track data and detect anomalies.

Key Features
Data Stream Simulation: Generates continuous data with noise and seasonal patterns.
Anomaly Detection Algorithm: Uses z-score to identify anomalies in real time.
Real-Time Processing: Processes data incrementally with a sliding window for efficiency.
Visualization: Displays the data stream and highlights anomalies with matplotlib.
Optimized for Speed: The sliding window ensures efficient computation, even with large datasets.
Error Handling: Robust validation to handle edge cases such as empty data streams and zero standard deviation.

