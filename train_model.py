import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset

data = pd.read_csv("dataset.csv")

# Features and target
X = data.drop("species", axis=1)
y = data["species"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = RandomForestClassifier()

# Train model
model.fit(X_train, y_train)

# Save model
with open("iris_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved successfully!")