
# Customer Churn Prediction – Final Report

## 1. Problem Statement
The objective of this project is to predict whether a telecom customer is likely to leave the company. Early churn prediction helps the business identify customers who may leave and take preventive actions.

## 2. Dataset
The Telco Customer Churn dataset contains 7,043 customer records and 21 columns. It includes customer demographics, services, contract details, payment methods and churn status.

## 3. Methodology
- Performed data cleaning and exploratory data analysis.
- Created additional features such as tenure_group and service_count.
- Applied numerical and categorical preprocessing.
- Used Logistic Regression, Random Forest and XGBoost models.
- Selected XGBoost as the final model.
- Handled class imbalance using scale_pos_weight.
- Evaluated the final model on held-out test data.

## 4. Results
The final XGBoost model was evaluated using:
- ROC-AUC Score
- F1 Score
- Confusion Matrix

The final evaluation values are available in the notebook output.

The model was saved as final_churn_model.joblib.

Predictions for new customers were generated and saved in predictions.csv.

## 5. Limitations
- Predictions depend on the quality of the available dataset.
- Customer behaviour may change over time.
- The model may not capture every reason for customer churn.
- Predictions should be used as decision support, not as guaranteed outcomes.

## 6. Business Recommendations
- Identify customers with high churn probability.
- Offer suitable retention plans and discounts.
- Improve customer support for customers who may leave.
- Monitor churn predictions regularly.
- Retrain the model when new customer data becomes available.

## Conclusion
The project successfully developed an XGBoost-based customer churn prediction system. It can help telecom businesses identify potential churners and plan customer retention strategies.
