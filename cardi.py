import streamlit as st
import numpy as np
import pickle 
import os

def app():
    st.header("Cardio Respiratory Disease Assessment")


    model_path = 'ML Dataset/cardio_trained_model.sav'
    if os.path.exists(model_path):
        model = pickle.load(open(model_path, 'rb'))
    else:
        st.error('Model file not found!')

  
    age = st.number_input('Age', min_value=1, max_value=120, value=25)
    gender = st.radio('Gender', options=['Male', 'Female'])
    height = st.number_input('Height (cm)', min_value=50, max_value=250, value=170)
    weight = st.number_input('Weight (kg)', min_value=10, max_value=300, value=70)
    ap_hi = st.number_input('Systolic Blood Pressure (ap_hi)', min_value=50, max_value=250, value=120)
    ap_lo = st.number_input('Diastolic Blood Pressure (ap_lo)', min_value=30, max_value=150, value=80)
    cholesterol = st.selectbox('Cholesterol Level', options=['Normal', 'Above Normal', 'Well Above Normal'])
    gluc = st.selectbox('Glucose Level', options=['Normal', 'Above Normal', 'Well Above Normal'])
    smoke = st.radio('Do you smoke?', options=['Yes', 'No'])
    alco = st.radio('Do you consume alcohol?', options=['Yes', 'No'])
    active = st.radio('Are you physically active?', options=['Yes', 'No'])
    # cardio = st.radio('Do you have cardiovascular disease?', options=['Yes', 'No'])

  
    gender = 1 if gender == 'Female' else 2
    cholesterol_mapping = {'Normal': 1, 'Above Normal': 2, 'Well Above Normal': 3}
    cholesterol = cholesterol_mapping[cholesterol]
    gluc_mapping = {'Normal': 1, 'Above Normal': 2, 'Well Above Normal': 3}
    gluc = gluc_mapping[gluc]
    smoke = 1 if smoke == 'Yes' else 0
    alco = 1 if alco == 'Yes' else 0
    active = 1 if active == 'Yes' else 0
    # cardio = 1 if cardio == 'Yes' else 0


    features = np.array([[age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active]])

    st.write(features)

    if st.button('Predict'):
        prediction = model.predict(features)
        if prediction[0] == 1:
            st.warning('The patient is at risk of heart disease.')
        else:
            st.success('The patient is not at risk of heart disease.')

