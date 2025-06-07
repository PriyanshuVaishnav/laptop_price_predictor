
import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("💻 Laptop Price Predictor")

# User Inputs
company = st.selectbox("Brand", ["Dell", "HP", "Apple", "Asus", "Acer"])
ram = st.selectbox("RAM (in GB)", [4, 8, 16, 32])
touchscreen = st.selectbox("Touchscreen", ["Yes", "No"])
ssd = st.selectbox("SSD (in GB)", [0, 128, 256, 512, 1024])
hdd = st.selectbox("HDD (in GB)", [0, 500, 1000, 2000])

# Convert 'Yes'/'No' to binary
touchscreen_binary = 1 if touchscreen == "Yes" else 0

# Prediction logic
if st.button("Predict Price"):
    try:
        model = pickle.load(open("model.pkl", "rb"))
        input_df = pd.DataFrame([[company, ram, touchscreen_binary, ssd, hdd]],
                                columns=["Company", "Ram", "Touchscreen", "SSD", "HDD"])
        prediction = model.predict(input_df)[0]
        st.success(f"Predicted Price: ₹{int(prediction)}")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
