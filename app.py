import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the saved model
model = joblib.load('model.sav')

st.title('Sales Predictor App')
st.write('This app predicts **Sales** based on advertising budgets for TV, Radio, and Newspaper.')

st.sidebar.header('Input Budgets')

# Input sliders
tv = st.sidebar.slider('TV Budget ($)', 0.0, 300.0, 150.0)
radio = st.sidebar.slider('Radio Budget ($)', 0.0, 50.0, 25.0)
newspaper = st.sidebar.slider('Newspaper Budget ($)', 0.0, 100.0, 30.0)

# Create a DataFrame for prediction
input_data = pd.DataFrame({
    'TV': [tv],
    'Radio': [radio],
    'Newspaper': [newspaper]
})

st.write('### Selected Input Features')
st.write(input_data)

# Predict button
if st.button('Predict Sales'):
    prediction = model.predict(input_data)[0]
    st.success(f'Predicted Sales: **${prediction:.2f}M**')
