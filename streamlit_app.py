import streamlit as st
from utils.data_utils import load_data, validate_and_clean_data
from utils.visualization_utils import plot_earnings_over_time, plot_earnings_contributions
from utils.model_utils import train_model, predict_earnings
import pandas as pd

st.set_page_config(page_title="Delivery Earnings Dashboard", layout="wide")

# Tabs for Navigation
tabs = st.tabs(["Home", "Upload Data", "Insights", "Predictions"])

# --- Home ---
with tabs[0]:
    st.title("Delivery Earnings Optimization Dashboard")
    st.write("Optimize your delivery earnings with insights and predictions.")

# --- Upload Data ---
with tabs[1]:
    st.header("Upload Delivery Data")
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    if uploaded_file:
        try:
            # Validate and clean the uploaded file
            df = pd.read_csv(uploaded_file)
            df = validate_and_clean_data(df)
            st.success("File uploaded and validated successfully!")
            st.write(df.head())  # Display the first few rows
            
            # Save cleaned data locally
            df.to_csv("./data/DoorDash_Mock_Data.csv", index=False)
        except Exception as e:
            st.error(f"Error: {e}")

# --- Insights ---
with tabs[2]:
    st.header("Earnings Insights")
    try:
        # Load and clean the data
        df = load_data()
        df = validate_and_clean_data(df)
        
        # Plot earnings over time
        st.plotly_chart(plot_earnings_over_time(df), use_container_width=True)
        
        # Plot earnings contributions
        st.plotly_chart(plot_earnings_contributions(df), use_container_width=True)
    except Exception as e:
        st.error(f"Error loading insights: {e}")

# --- Predictions ---
with tabs[3]:
    st.header("Earnings Predictions")
    try:
        # Input widgets
        base_pay = st.number_input("Base Pay", 0.0, 100.0, step=0.1)
        tips = st.number_input("Tips", 0.0, 100.0, step=0.1)
        peak_pay = st.number_input("Peak Pay", 0.0, 100.0, step=0.1)
        adjustments = st.number_input("Adjustments", 0.0, 100.0, step=0.1)
        
        if st.button("Predict Earnings"):
            prediction = predict_earnings(base_pay, tips, peak_pay, adjustments)
            st.success(f"Predicted Earnings: ${prediction:.2f}")
    except Exception as e:
        st.error(f"Prediction error: {e}")
