import streamlit as st
import pandas as pd

st.title("Patient Data Input Form")

# Collect user inputs

data = {}
data['Age'] = st.number_input("Age", min_value=0, max_value=120, value=30)
data['Gender'] = st.selectbox("Gender", ['Male', 'Female'])
data['Geographic Location'] = st.selectbox("Geographic Location", ['Urban', 'Suburban', 'Rural'])
data['Chronic Conditions'] = st.number_input("Number of Chronic Conditions", min_value=0, max_value=20)
data['Past Medical Procedures'] = st.number_input("Past Medical Procedures", min_value=0, max_value=20)
data['Comorbidities'] = st.number_input("Comorbidities", min_value=0, max_value=10)
data['Frequency of Visits'] = st.number_input("Frequency of Visits", min_value=0, max_value=50)
data['Appointment Adherence'] = st.number_input("Appointment Adherence (0-1)", min_value=0.0, max_value=1.0, step=0.01)
data['Follow-Up Compliance'] = st.number_input("Follow-Up Compliance (0-1)", min_value=0.0, max_value=1.0, step=0.01)
data['Preventive Care'] = st.number_input("Preventive Care Visits", min_value=0, max_value=50)
data['Patient Portal Usage'] = st.number_input("Patient Portal Usage Frequency", min_value=0, max_value=50)
data['Communication Frequency'] = st.number_input("Communication Frequency", min_value=0, max_value=50)
data['Feedback and Surveys'] = st.number_input("Feedback Score (0-1)", min_value=0.0, max_value=1.0, step=0.01)
data['Type of Treatments'] = st.number_input("Number of Treatment Types", min_value=0, max_value=20)
data['Treatment Outcomes'] = st.selectbox("Treatment Outcomes", ['Failure', 'Ongoing', 'Success'])
data['Duration of Care'] = st.number_input("Duration of Care (days)", min_value=0, max_value=1000)
data['Payment History'] = st.number_input("Payment History Score (0-1)", min_value=0.0, max_value=1.0, step=0.01)
data['Insurance Coverage'] = st.selectbox("Insurance Coverage", ['Basic', 'Standard', 'Premium'])
data['Out-of-Pocket Expenses'] = st.number_input("Out-of-Pocket Expenses", min_value=0.0, step=0.01)
data['Income Level'] = st.number_input("Income Level", min_value=0)
data['Education Level'] = st.selectbox("Education Level", ['High School', 'Bachelor', 'Master', 'PhD'])
data['Smoking Status'] = st.selectbox("Smoking Status", ['Yes', 'No'])
data['Alcohol Consumption'] = st.selectbox("Alcohol Consumption", ['None', 'Moderate', 'Heavy'])
data['Exercise Frequency'] = st.number_input("Exercise Frequency (per week)", min_value=0, max_value=14)
data['Dietary Habits'] = st.selectbox("Dietary Habits", ['Healthy', 'Poor'])
data['Mental Health'] = st.selectbox("Mental Health", ['Good', 'Poor'])
data['Stress Levels'] = st.number_input("Stress Levels (0-1)", min_value=0.0, max_value=1.0, step=0.01)
data['Wait Times'] = st.number_input("Average Wait Times (minutes)", min_value=0.0, step=0.1)
data['Facility Ratings'] = st.number_input("Facility Ratings (0-5)", min_value=0.0, max_value=5.0, step=0.1)
data['Staff Interactions'] = st.number_input("Staff Interaction Score (0-5)", min_value=0.0, max_value=5.0, step=0.1)
data['Accessibility'] = st.number_input("Accessibility Score (0-5)", min_value=0.0, max_value=5.0, step=0.1)
data['Referral Source'] = st.selectbox("Referral Source", ['Advertisement', 'Online Search', 'Walk-in', 'Referral'])
data['Family History'] = st.selectbox("Family History of Disease", ['Yes', 'No'])
data['Loyalty Program Participation'] = st.number_input("Loyalty Program Participation (0 or 1)", min_value=0, max_value=1)

# Encoding categorical values
def encode_inputs(data):
    mapping = {
        'Gender': {'Male': 1, 'Female': 0},
        'Geographic Location': {'Urban': 2, 'Suburban': 1, 'Rural': 0},
        'Treatment Outcomes': {'Failure': 0, 'Ongoing': 1, 'Success': 2},
        'Insurance Coverage': {'Basic': 0, 'Standard': 1, 'Premium': 2},
        'Education Level': {'High School': 0, 'Bachelor': 1, 'Master': 2, 'PhD': 3},
        'Smoking Status': {'Yes': 1, 'No': 0},
        'Alcohol Consumption': {'None': 0, 'Moderate': 1, 'Heavy': 2},
        'Dietary Habits': {'Healthy': 1, 'Poor': 0},
        'Mental Health': {'Good': 1, 'Poor': 0},
        'Referral Source': {'Advertisement': 0, 'Online Search': 1, 'Walk-in': 2, 'Referral': 3},
        'Family History': {'Yes': 1, 'No': 0},
    }
    
    for key, value in mapping.items():
        data[key] = value[data[key]]
    return data

# Submit button
if st.button("Submit"):
    encoded_data = encode_inputs(data)
    df = pd.DataFrame([encoded_data])
    st.write("### Encoded Data Ready for Model:")
    st.dataframe(df)
    st.success("Data is ready! You can now use it for prediction.")
