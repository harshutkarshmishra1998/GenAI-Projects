import os
from pathlib import Path
import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle

# Load the trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), '6-model.h5')
model = tf.keras.models.load_model(MODEL_PATH)
# model = tf.keras.models.load_model('6-model.h5')

# Base directory of the current script
BASE_DIR = Path(__file__).parent

# Paths to files
gender_encoder_path = BASE_DIR / "3-label_encoder_gender.pkl"
geo_encoder_path = BASE_DIR / "4-onehot_encoder_geo.pkl"
scaler_path = BASE_DIR / "5-scaler.pkl"

# Load the encoders and scaler
with open(gender_encoder_path, 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open(geo_encoder_path, 'rb') as file:
    onehot_encoder_geo = pickle.load(file)

with open(scaler_path, 'rb') as file:
    scaler = pickle.load(file)

## streamlit app
st.title('Customer Churn Prediction')

# User input
geography = st.selectbox('Geography', onehot_encoder_geo.categories_[0])
gender = st.selectbox('Gender', label_encoder_gender.classes_)
age = st.slider('Age', 18, 92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])

# Prepare the input data
input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})

# One-hot encode 'Geography'
geo_encoded = onehot_encoder_geo.transform([[geography]]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehot_encoder_geo.get_feature_names_out(['Geography']))

# Combine one-hot encoded columns with input data
input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

# Scale the input data
input_data_scaled = scaler.transform(input_data)


# Predict churn
prediction = model.predict(input_data_scaled)
prediction_proba = prediction[0][0]

st.write(f'Churn Probability: {prediction_proba:.2f}')

if prediction_proba > 0.5:
    st.write('The customer is likely to churn.')
else:
    st.write('The customer is not likely to churn.')
