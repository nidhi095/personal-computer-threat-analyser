import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load data
df = pd.read_csv("data/traffic.csv")

# Encode labels
df["Label"] = df["Label"].astype("category")
df["Label_Code"] = df["Label"].cat.codes

# Features and target
X = df[["Protocol", "Length"]]
y = df["Label_Code"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model and label mapping
joblib.dump(model, "model.pkl")
df[["Label", "Label_Code"]].drop_duplicates().to_csv("label_mapping.csv", index=False)

print("Model trained and saved.")
