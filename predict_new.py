
import pandas as pd
import joblib

print("========== NEW CUSTOMER CHURN PREDICTION ==========")

model = joblib.load("final_churn_model.joblib")

new_data = pd.read_csv("new_customers.csv")

customer_ids = new_data["customerID"]

X_new = new_data.drop(columns=["customerID"])

predictions = model.predict(X_new)
probabilities = model.predict_proba(X_new)[:, 1]

results = pd.DataFrame({
    "customerID": customer_ids,
    "Predicted_Churn": ["Yes" if p == 1 else "No" for p in predictions],
    "Churn_Probability": probabilities
})

results.to_csv("predictions.csv", index=False)

print("Total Customers:", len(results))
print("Predictions Generated Successfully")
print("File Saved: predictions.csv")
print("\n========== PREDICTION COMPLETED ==========")
