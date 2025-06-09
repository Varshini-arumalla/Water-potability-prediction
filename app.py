import streamlit as st
import numpy as np
import pickle

# Load the trained model and scaler
model = pickle.load(open('water_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("🚰 Water Potability Prediction App")
st.write("Enter the water sample measurements to check if the water is potable.")

# Input fields for water quality parameters
ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0, format="%.2f")
hardness = st.number_input("Hardness (mg/L)", min_value=0.0, max_value=500.0, value=150.0, format="%.2f")
solids = st.number_input("Solids (ppm)", min_value=0.0, max_value=50000.0, value=10000.0, format="%.2f")
chloramines = st.number_input("Chloramines (ppm)", min_value=0.0, max_value=15.0, value=6.0, format="%.2f")
sulfate = st.number_input("Sulfate (mg/L)", min_value=0.0, max_value=500.0, value=300.0, format="%.2f")
conductivity = st.number_input("Conductivity (μS/cm)", min_value=0.0, max_value=1000.0, value=400.0, format="%.2f")
organic_carbon = st.number_input("Organic Carbon (ppm)", min_value=0.0, max_value=30.0, value=10.0, format="%.2f")
trihalomethanes = st.number_input("Trihalomethanes (μg/L)", min_value=0.0, max_value=150.0, value=66.0, format="%.2f")
turbidity = st.number_input("Turbidity (NTU)", min_value=0.0, max_value=10.0, value=4.0, format="%.2f")

# Predict button
if st.button("Predict Potability"):
    input_features = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity,
                                organic_carbon, trihalomethanes, turbidity]])
    input_scaled = scaler.transform(input_features)
    result = model.predict(input_scaled)

    if result[0] == 1:
        st.success("✅ The water is *potable* (safe to drink).")
    else:
        st.error("⚠ The water is *not potable*
        st.success("✅ The water is *potable* (safe to drink).")
    else:
        st.error("⚠ The water is *not potable* (unsafe to drink).")