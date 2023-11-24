import streamlit as st
import numpy as np
import joblib as jb
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the Random Forest model and scaler
model = jb.load('random_forest_model.pkl')
scaler = jb.load('scaler.pkl')

# Streamlit app
def run():
    with st.form('patient_form'):
        st.write('# BidiBomBom App')
        
        # Get input from the user
        Age = st.slider("Age", min_value=20, max_value=80, value=40)
        Sex = st.radio("Sex", options=["Male", "Female"], index=0)
        st.write('Optimal <120  Normal 120-129  Hypertension >150')
        RestingBP = st.slider("# Resting Blood Pressure [mm Hg]", min_value=80, max_value=200, value=120)
        
        st.write('Desirable <200 === Borderline High 200-239 === High >240')
        Cholesterol = st.slider("# Total Cholesterol:", min_value=100, max_value=400, value=200)
        
        FastingBS = st.radio("# Fasting Blood Sugar > 120 mg/dL", options=["No", "Yes"], index=0)
        MaxHR = st.slider("# Maximum Heart Rate", min_value=60, max_value=220, value=150)

        st.write('Oldpeak is an indicator in ECG test; leave it at 0 if you are unsure')
        Oldpeak = st.slider("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, max_value=3.0, step=0.5, value=0.5)

        st.write('# Chest Pain: Please only select one answer')
        st.write('1. Question below regarding patient history with Chest pain; please only select one box if the conditions are met')
        # Chest Pain Type
        ChestPainType_ASY = st.checkbox("NORMAL no pain.")
        ChestPainType_ATA = st.checkbox("Chest pain that doesn't quite fit the typical pattern seen in heart-related issues.")
        ChestPainType_NAP = st.checkbox("Heartburn, inflammation, acid reflux.")
        ChestPainType_TA = st.checkbox("Heart-related chest pain, radiate to arms, neck, jaw, shoulder.")

        st.write('# Chest Pain while exercising')
        # Exercise Angina
        ExerciseAngina_N = st.checkbox("No Chest pain while exercise")
        ExerciseAngina_Y = st.checkbox("Chest pain while exercise")

        # Convert checkbox values to numerical values
        ChestPainType_ASY = 1 if ChestPainType_ASY else 0
        ChestPainType_ATA = 1 if ChestPainType_ATA else 0
        ChestPainType_NAP = 1 if ChestPainType_NAP else 0
        ChestPainType_TA = 1 if ChestPainType_TA else 0

        ExerciseAngina_N = 1 if ExerciseAngina_N else 0
        ExerciseAngina_Y = 1 if ExerciseAngina_Y else 0

        # Button to trigger the prediction
        submit_button = st.form_submit_button("Predict")

    # Make predictions when the form is submitted
    if submit_button:
        # Convert categorical variables to numerical values
        Sex = 1 if Sex == "Male" else 0
        FastingBS = 1 if FastingBS == "Yes" else 0

        # Prepare input data for prediction
        input_data = np.array([[Age, Sex, RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak,
                                ChestPainType_ASY, ChestPainType_ATA, ChestPainType_NAP, ChestPainType_TA,
                                ExerciseAngina_N, ExerciseAngina_Y]])

        # Scale the input data using the same scaler
        input_data_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_data_scaled)

        # Display the result
        st.write('## Prediction Result')
        if prediction[0] == 1:
            st.warning("The model predicts that the patient is HIGH RISK.")
            st.warning("High Risk Detected! Take appropriate action.")
            st.write("CDC heart disease information: "
             "https://www.cdc.gov/heartdisease/index.htm")
            st.warning("Disclaimer I am not a doctor.  Go get a check up")
         
        else:
            st.success("The model predicts that the patient is LOW RISK.")
            st.write("CDC heart disease information: "
         "https://www.cdc.gov/heartdisease/index.htm")
            st.success("Disclaimer I am not a doctor.  Go get a check up")
      
            st.balloons()

    st.markdown()

    
if __name__ == "__main__":
    run()