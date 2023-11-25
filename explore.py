import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path


st.set_page_config(
    page_title = 'Heart Failure Risk Prediction',
    layout = 'centered'
)
url = "https://raw.githubusercontent.com/leedthanh/api/main/heart.csv"

def run() :
    dataset_heart_risk = pd.read_csv(url)

    st.title('Heart Failure Prediction Exploratory Data Analysis')

    st.subheader('Data Source')
    st.write('https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction')
    st.write('A credit to Md Yousuf Reja and Maria Parra')
    
    st.markdown('---')

    st.write('### Scatter Plot for Heart Disease Visualization')
    st.write('Red points represent individuals with heart disease, blue points represent those without.')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    fig_scatter = plt.figure(figsize=(10, 6))
    plt.scatter(x=dataset_heart_risk.Age[dataset_heart_risk.HeartDisease == 1], 
                y=dataset_heart_risk.MaxHR[(dataset_heart_risk.HeartDisease == 1)], c="red")
    plt.scatter(x=dataset_heart_risk.Age[dataset_heart_risk.HeartDisease == 0], 
                y=dataset_heart_risk.MaxHR[(dataset_heart_risk.HeartDisease == 0)])
    plt.legend(["Disease", "Not Disease"])
    plt.xlabel("Age")
    plt.ylabel("Maximum Heart Rate")

    st.pyplot(fig_scatter)

    st.markdown('---')
    st.write('### Heart Disease Frequency for Ages')
    fig_frequency, ax = plt.subplots(figsize=(10, 8))
    pd.crosstab(dataset_heart_risk.Age, dataset_heart_risk.HeartDisease).plot(kind="bar", ax=ax)  # Corrected variable name 'df' to 'dataset_heart_risk'
    ax.set_title('Heart Disease Frequency for Ages')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    st.pyplot(fig_frequency)

    st.markdown('---')

    st.write('### Numerical Data Histogram')
    st.write('Notes : Oldpeak is numeric value measured in depression'
             'FastingBs = fasting blood sugar level'
             'MaxHR = max heart rate'
             'RestingBP = resting blood pressure')
    
    hist_choice = st.selectbox('Select column : ', ('Age', 'Cholesterol', 'RestingBP', 'FastingBS', 
                                                'MaxHR','HeartDisease','RestingECG','ExerciseAngina',
                                                'Oldpeak','ST_Slope','Sex','ChestPainType'
                                            ))
    fig_one = plt.figure(figsize=(15,5))
    sns.histplot(x = dataset_heart_risk[hist_choice], bins=30, kde = True)
    st.pyplot(fig_one)

    st.markdown('---')

    # membuat heatmap correlation= antar data numerik
    numeric_column = ['Age', 'Cholesterol', 'RestingBP', 'FastingBS', 
                        'FastingBS', 'MaxHR']
    
    st.write('### Numerical Data Heatmap Correlation')
    fig_two = plt.figure(figsize=(20,20))
    sns.heatmap(dataset_heart_risk[numeric_column].corr(), cmap="YlGnBu", annot=True) 
    st.pyplot(fig_two)


if __name__ == '__main__':
    run()
