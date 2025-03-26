import streamlit as st
import pandas as pd
import joblib
import json

# Load model, scaler, and feature names
model = joblib.load('hospital_model.pkl')
scaler = joblib.load('scaler.pkl')

try:
    with open('feature_names.json', 'r') as f:
        feature_names = json.load(f)
except FileNotFoundError:
    st.error("feature_names.json not found. Please ensure it is in the same directory.")
    st.stop()

st.title("🏥 Hospital Management & Patient Loyalty Prediction")
st.write("Enter the following details:")

# Collect user input dynamically
user_input = {}
for feature in feature_names:
    value = st.number_input(f"{feature}", step=1.0)
    user_input[feature] = value

if st.button("Predict Loyalty Score"):
    input_df = pd.DataFrame([user_input])
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)
    st.success(f"✅ Predicted Loyalty Score: {prediction[0]}")

st.sidebar.header("ℹ️ About")
st.sidebar.info("This app predicts customer loyalty scores for healthcare customers based on provided input data.")
