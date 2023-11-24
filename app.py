import streamlit as st
import explore  # Assuming the script is named explore.py
import prediction as predict_explore
import prediction as heart
page = st.sidebar.selectbox('Select page: ', ('Use Machine Learning','Explore The Dataset'))

if page == 'Use Machine Learning':
    heart.run()
else:
    explore.run()