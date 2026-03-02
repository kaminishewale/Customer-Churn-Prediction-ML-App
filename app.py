import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load saved model and columns
# -----------------------------
model = joblib.load("churn_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.set_page_config(page_title="Customer Churn Prediction", layout="centered")

st.title("📊 Customer Churn Prediction App")
st.write("Enter customer details below to predict churn probability.")

st.divider()

# -----------------------------
# User Inputs
# -----------------------------

tenure = st.slider("Tenure (Months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

paperless_billing = st.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

st.divider()

# -----------------------------
# Prediction Logic
# -----------------------------
if st.button("Predict Churn"):

    # Create empty dictionary with all model columns
    input_dict = dict.fromkeys(model_columns, 0)

    # Fill numeric values
    if "Tenure Months" in input_dict:
        input_dict["Tenure Months"] = tenure

    if "Monthly Charges" in input_dict:
        input_dict["Monthly Charges"] = monthly_charges

    # Fill categorical dummy variables safely
    contract_col = f"Contract_{contract}"
    internet_col = f"Internet Service_{internet_service}"
    paperless_col = f"Paperless Billing_{paperless_billing}"

    if contract_col in input_dict:
        input_dict[contract_col] = 1

    if internet_col in input_dict:
        input_dict[internet_col] = 1

    if paperless_col in input_dict:
        input_dict[paperless_col] = 1

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Predict
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠ Customer is likely to CHURN")
    else:
        st.success("✅ Customer is likely to STAY")

    st.write(f"Churn Probability: **{probability:.2%}**")