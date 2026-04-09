import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle
from feature_extraction import extract_features

# Load dataset
data = pd.read_csv("dataset.csv")

# Map labels
data['Label'] = data['Label'].map({'bad': 1, 'good': 0})

# Extract features
X = [extract_features(url) for url in data['URL']]
y = data['Label']

# --- Optional check: all features same length ---
lengths = [len(f) for f in X]
print("Unique feature lengths:", set(lengths))  # should print {18}

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train RandomForest
model = RandomForestClassifier(
    n_estimators=50,
    max_depth=10,
    min_samples_split=5,
    class_weight='balanced',
    random_state=42
)
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
print("✅ Model trained and saved successfully")

# --- Evaluate ---
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=['Legitimate', 'Phishing']))
