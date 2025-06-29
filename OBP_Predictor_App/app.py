import streamlit as st
import numpy as np
import pickle

# Load model and scaler
with open('model_bundle.pkl', 'rb') as f:
    bundle = pickle.load(f)
    scaler = bundle['scaler']
    model = bundle['model']

st.title("MLB OBP Predictor")
st.write("Enter values for AVG and SLG to predict OBP.")

avg = st.slider("Batting Average (AVG)", 0.100, 0.600, 0.250, 0.001, format="%.3f")
slg = st.slider("Slugging Percentage (SLG)", 0.200, 0.800, 0.400, 0.001, format="%.3f")

if st.button("Predict OBP"):
    input_data = np.array([[avg, slg]])
    input_scaled = scaler.transform(input_data)
    obp = model.predict(input_scaled)[0]
    st.success(f"Predicted OBP: {obp:.3f}")