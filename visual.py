import streamlit as st
from streamlit_extras.let_it_rain import rain
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


def app():
    st.subheader('Visualization')



    df=pd.read_csv("Submission.csv")
    st.subheader("Expolatory Data Analysis")
    submenu=['Descriptive Analsis','Plots']
    choice=st.sidebar.selectbox("SubMenu",submenu)
    if choice == 'Descriptive Analsis':
        st.subheader("This is our data")
        st.dataframe(df)
        st.subheader("Here is Statistical Analysis of All Numerical Data")
        st.dataframe(df.describe())
        col1,col2,col3=st.columns(3)
        with col1:
            st.subheader("Data Types")
            st.dataframe(df.dtypes)
        with col2:
            st.subheader("Basic Information about Data")
            # st.image("info.png")
        with col3:
            st.subheader("Details")
            with st.expander("Column Gender"):
                st.dataframe(df['gender'].value_counts())
        with col3:
            with st.expander("Column smoke"):
                st.dataframe(df['smoke'].value_counts())
        with col3:
            with st.expander("Alco"):
                st.dataframe(df["alco"].value_counts())
        with col3:	
            with st.expander("Active"):
                st.dataframe(df["active"].value_counts())
    else:
        st.subheader("Let's start with Data Visualization")
        st.image("Images/plots.jpeg")
        st.write("""EDA Using Plots """)


        st.write("""
        Data visualization is the graphical representation of information and data. By using visual elements 
        like charts, graphs, and maps, data visualization tools provide an accessible way to see and understand trends, 
        outliers, and patterns in data.""")

        st.write('Distribution of Target Variable')                
        st.image('Images/target.jpg')

        st.write('Distribution of Gender Age')
        st.image('Images/genderage.jpg')

        st.write('Distribution of Smoke')
        st.image('Images/smoke.jpg')

        st.write('HeatMap')
        st.image('Images/heat.jpg')


         
    


  


