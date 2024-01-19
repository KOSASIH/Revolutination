import pandas as pd
from sklearn.ensemble import IsolationForest

# Load historical user data
data = pd.read_csv("user_data.csv")

# Train anomaly detection model
model = IsolationForest(contamination=0.01)
model.fit(data)


# Real-time monitoring
def detect_anomaly(user_data):
    # Predict anomaly score
    anomaly_score = model.decision_function(user_data)

    # Set anomaly threshold
    threshold = -0.5

    # Check if anomaly score exceeds threshold
    if anomaly_score < threshold:
        # Send alert message
        alert_message = "Anomaly detected! Please review your account activity."
        return alert_message
    else:
        return None


# Sample user data
user_data = pd.DataFrame({"transaction_amount": [1000, 200, 3000, 500]})

# Detect anomaly
alert = detect_anomaly(user_data)

if alert:
    print(alert)
else:
    print("No anomaly detected.")
