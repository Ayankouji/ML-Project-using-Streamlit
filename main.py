import streamlit as st
import numpy as np
import pandas as pd
import pickle 
from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv
from streamlit_extras.let_it_rain import rain
load_dotenv()


st.set_page_config(
    page_title="Monsoon Health Risk Assessment",
)


st.title('Monsoon Health Risk Analysis ')
st.image('Images/heaart.jpg')

model_path = 'ML Dataset/cardio_trained_model.sav'

if os.path.exists(model_path):
    model = pickle.load(open(model_path, 'rb'))
else:
    st.error('Model file not found!')

import home,visual, cardi,dashboard



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Workers Health Care Prediction',
                options=['Home', 'Visualization', 'Cardio Respiratory Disease','Dashboard'],
                icons=['house-fill', 'bar-chart-fill', 'heart-fill'],
                menu_icon='eye-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "grey"},
                    "nav-link-selected": {"background-color": "#c7f2f2"},
                }
            )

        if app == "Home":
            home.app()
        elif app == "Visualization":
            visual.app()
        elif app == "Cardio Respiratory Disease":
            cardi.app()
        elif app == 'dashboard':
            dashboard.app()
      
            


app_instance = MultiApp()
app_instance.run()

rain(emoji="💧", font_size=54,

falling_speed=5,animation_length='infinite')
