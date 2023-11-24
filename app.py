import streamlit as st
import explore  # Assuming the script is named explore.py
import prediction as predict_explore
import prediction as heart
page = st.sidebar.selectbox('Select page: ', ('explore', 'prediction'))

if page == 'explore':
    explore.run()
else:
    heart.run()