import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Card Fraud Detection")
st.write(
    "Machine Learning based fraud detection using Logistic Regression"
)

model = joblib.load("fraud_model.pkl")
scaler = joblib.load("scaler.pkl")

st.success("Trained model loaded successfully")

st.divider()

st.subheader("📌 About the Model")

col1, col2, col3 = st.columns(3)

col1.metric("Algorithm", "Logistic Regression")
col2.metric("Features", "30")
col3.metric("Output", "Fraud / Legitimate")

st.divider()

st.subheader("🔍 Check a Transaction")

st.write(
    "Enter the transaction details below. "
    "For demonstration purposes, unspecified PCA features "
    "are initialized to zero."
)

time = st.number_input(
    "Transaction Time",
    min_value=0.0,
    value=10000.0,
    step=100.0
)

amount = st.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=100.0,
    step=10.0
)

st.subheader("PCA Features")

features = {}

for i in range(1, 29):

    features[f"V{i}"] = st.number_input(
        f"V{i}",
        value=0.0,
        format="%.6f"
    )

if st.button(
    "Check Transaction",
    type="primary"
):

    transaction = {
        "Time": time
    }

    for i in range(1, 29):
        transaction[f"V{i}"] = features[f"V{i}"]

    transaction["Amount"] = amount

    input_data = pd.DataFrame(
        [transaction]
    )

    input_scaled = scaler.transform(
        input_data
    )

    prediction = model.predict(
        input_scaled
    )[0]

    probability = model.predict_proba(
        input_scaled
    )[0][1]

    st.divider()

    if prediction == 1:

        st.error(
            "⚠️ FRAUDULENT TRANSACTION DETECTED"
        )

    else:

        st.success(
            "✅ TRANSACTION APPEARS LEGITIMATE"
        )

    st.metric(
        "Fraud Probability",
        f"{probability * 100:.2f}%"
    )

    st.progress(
        float(probability)
    )

st.divider()

st.subheader("ℹ️ Project Information")

st.write(
    "This project uses Logistic Regression to classify "
    "credit card transactions as fraudulent or legitimate. "
    "The input data is standardized using StandardScaler "
    "before prediction."
)