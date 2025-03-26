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

# Define categorical features and their options
categorical_inputs = {
    "Gender": ["Male", "Female"],
    "Geographic Location": ["Urban", "Suburban", "Rural"],
    "Smoking Status": ["Yes", "No"],
    "Alcohol Consumption": ["None", "Moderate", "Heavy"],
    "Dietary Habits": ["Healthy", "Poor"],
    "Mental Health": ["Good", "Poor"],
    "Education Level": ["High School", "Master", "PhD"],
    "Treatment Outcomes": ["Failure", "Ongoing", "Success"],
    "Insurance Coverage": ["Basic", "Standard", "Premium"],
    "Referral Source": ["Advertisement", "Online Search", "Walk-in", "Referral"],
    "Family History": ["Yes", "No"]
}

user_input = {}

# Collect input from user
for feature in feature_names:
    if feature in categorical_inputs:
        value = st.selectbox(f"{feature}", categorical_inputs[feature])
        user_input[feature] = value
    else:
        value = st.number_input(f"{feature}", step=1.0)
        user_input[feature] = value

# One-hot encode categorical inputs for prediction (if your model was trained with encoding)
input_df = pd.DataFrame([user_input])
input_encoded = pd.get_dummies(input_df)

# Align columns with model feature names
for col in feature_names:
    if col not in input_encoded.columns:
        input_encoded[col] = 0

# Predict on scaled numerical input
input_scaled = scaler.transform(input_encoded[feature_names])
if st.button("Predict Loyalty Score"):
    prediction = model.predict(input_scaled)
    st.success(f"✅ Predicted Loyalty Score: {prediction[0]}")

st.sidebar.header("ℹ️ About")
st.sidebar.info("This app predicts customer loyalty scores for healthcare customers based on provided input data.")
