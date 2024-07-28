import streamlit as st
import numpy as np
import pandas as pd
import pickle 

loaded_model = pickle.load(open('cardio_trained_model.sav','rb'))

def cardio_pred(pred):
    pred_array = np.array(pred)

    pred_reshaped = pred_array.reshape(1,-1)

    prediction = loaded_model.predict(pred_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        print('the patient is safe from heart diseases')
    else:
        print('the patient might have heart related issues in the future')

def main():
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

    diagnosis = ''

    if st.button('Test Results:'):
        diagnosis = cardio_pred([age,gender,height,weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active])

    st.info(diagnosis)