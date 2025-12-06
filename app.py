import  streamlit as st
import joblib 
import numpy as np

#load the saved regression model 
model= joblib.load ('regression-model_.joblib')
# streamlit app Ui
st.title ('Job Package Prediction based on CGPA')
st.write ('Enter your CGPA to predict the  expected job package:')
#user  input for  CGPA
cgpa = st.number_input('CGPA',min_value=-0.0,max_value =10.0,step =0.1)
#Predict button
if st.button ('Predict_Package'):
    #prepare input data for the model
    input_data =np.array ([[cgpa]])
    #Predict the Package
    prediction= model .predict(input_data)
    predicted_value =float(prediction[0]) #Convert  Numpy value to float
    #show the result
    st.success(f'Predicted Package: ${predicted_value:,.2f}LPA')
    