import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
import pickle

# Load the trained model
model = pickle.load(open('/content/model.sav','rb'))

st.title("Customer Churn Prediction App")

# Create input fields for the user to enter data

st.info("Input data below")

st.subheader("Demographic data")
SeniorCitizen = st.selectbox('Senior Citizen', [0,1])
gender = st.selectbox("Gender", ("Male", "Female"))
Partner = st.selectbox("Partner", ("Yes", "No"))
Dependents = st.selectbox('Dependents', ('Yes', 'No'))

st.subheader("Payment data")
tenure = st.text_input('Number of months the customer has stayed with the company')
Contract = st.selectbox('Contract', ('Month-to-month', 'One year', 'Two years'))
PaperlessBilling = st.selectbox('Paperless Billing', ('Yes', 'No'))
PaymentMethod = st.selectbox('Payment Method', ('Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'))
MonthlyCharges = st.text_input('The amount charged to the customer monthly')
TotalCharges = st.text_input('The total amount charged to the customer')

st.subheader("Services signed up for")
MultipleLines = st.selectbox("Does the customer have multiple lines", ('Yes', 'No', 'No phone service'))
PhoneService = st.selectbox('Phone Service', ('Yes', 'No'))
InternetService = st.selectbox("Does the customer have internet service", ('DSL', 'Fiber optic', 'No'))
OnlineSecurity = st.selectbox("Does the customer have online security", ('Yes', 'No', 'No internet service'))
OnlineBackup = st.selectbox("Does the customer have online backup", ('Yes', 'No', 'No internet service'))
DeviceProtection = st.selectbox("Device Protection", ("No", "Yes", "No Internet Service"))
TechSupport = st.selectbox("Does the customer have technology support", ('Yes', 'No', 'No internet service'))
StreamingTV = st.selectbox("Does the customer stream TV", ('Yes', 'No', 'No internet service'))
StreamingMovies = st.selectbox("Does the customer stream movies", ('Yes', 'No', 'No internet service'))

tenure = float(tenure) if tenure != '' else 0
MonthlyCharges = float(MonthlyCharges) if MonthlyCharges != '' else 0
TotalCharges = float(TotalCharges) if TotalCharges != '' else 0

gender = 1 if gender == "Male" else 0
Partner = 1 if Partner == "Yes" else 0
dependents = 1 if Dependents == "Yes" else 0
Contract = 0 if Contract == "Month-to-month" else 1 if Contract == "One year" else 2
PaperlessBilling = 1 if PaperlessBilling == "Yes" else 0
PaymentMethod = 0 if PaymentMethod == "Electronic check" else 1 if PaymentMethod == "Mailed check" else 2 if PaymentMethod == "Bank transfer (automatic)" else 3
PhoneService = 1 if PhoneService == "Yes" else 0
MultipleLines = 0 if MultipleLines == "No" or MultipleLines == "No phone service" else 1
InternetService = 0 if InternetService == "No" else 1 if InternetService == "Fiber optic" else 2
OnlineSecurity = 0 if OnlineSecurity == "No" or OnlineSecurity == "No internet service" else 1
OnlineBackup = 0 if OnlineBackup == "No" or OnlineBackup == "No internet service" else 1
DeviceProtection = 0 if DeviceProtection == "No" or DeviceProtection == "No internet service" else 1
TechSupport = 0 if TechSupport == "No" or TechSupport == "No internet service" else 1
StreamingTV = 0 if StreamingTV == "No" or StreamingTV == "No internet service" else 1
StreamingMovies = 0 if StreamingMovies == "No" or StreamingMovies == "No internet service" else 1

# Make predictions
input_data = pd.DataFrame({
    'gender': [gender],
    'SeniorCitizen': [SeniorCitizen],
    'Partner': [Partner],
    'Dependents': [dependents],
    'tenure': [tenure],
    'PhoneService': [PhoneService],
    'MultipleLines': [MultipleLines],
    'InternetService': [InternetService],
    'OnlineSecurity': [OnlineSecurity],
    'OnlineBackup': [OnlineBackup],
    'DeviceProtection': [DeviceProtection],
    'TechSupport': [TechSupport],
    'StreamingTV': [StreamingTV],
    'StreamingMovies': [StreamingMovies],
    'Contract': [Contract],
    'PaperlessBilling': [PaperlessBilling],
    'PaymentMethod': [PaymentMethod],
    'MonthlyCharges': [MonthlyCharges],
    'TotalCharges': [TotalCharges]  
})

st.write('Overview of input is shown below')
st.write(input_data)

# Standardize numerical features
numerical_features =['tenure', 'MonthlyCharges', 'TotalCharges']
scaler=MinMaxScaler()
input_data[numerical_features]=scaler.fit_transform(input_data[numerical_features])


if st.button("Prediction"):
  prediction = model.predict(input_data)
  if prediction[0] == 1:
    st.write("The customer will terminate the service")
  else:
    st.write("The customer is happy with the Services")