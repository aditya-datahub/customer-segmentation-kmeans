import streamlit as st
import pandas as pd
import numpy as np
import joblib

kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Customer Segmentation App")
st.write("Enter customer details to predict the segment.")

# --- Input Fields ---
age = st.number_input("Age", min_value=18, max_value=100, value=35)
income = st.number_input("Annual Income ($)", min_value=0, max_value=200000, value=50000)
total_spending = st.number_input("Total Spending ($)", min_value=0, max_value=5000, value=500)
num_web_purchases = st.number_input("Number of Web Purchases", min_value=0, max_value=50, value=5)
num_store_purchases = st.number_input("Number of Store Purchases", min_value=0, max_value=50, value=5)
num_deals_purchases = st.number_input("Number of Deal Purchases", min_value=0, max_value=50, value=2)  # ✅ ADD THIS
num_web_visits = st.number_input("Web Visits per Month", min_value=0, max_value=30, value=4)
recency = st.number_input("Recency (days since last purchase)", min_value=0, max_value=365, value=30)

# --- Prepare Input ---
input_data = pd.DataFrame({
    "Age": [age],
    "Income": [income],
    "Total_Spending": [total_spending],
    "NumWebPurchases": [num_web_purchases],
    "NumStorePurchases": [num_store_purchases],
    "NumDealsPurchases": [num_deals_purchases],  # ✅ ADD THIS
    "NumWebVisitsMonth": [num_web_visits],
    "Recency": [recency]
})

input_scaled = scaler.transform(input_data)

# --- Predict ---
if st.button("Predict Segment"):
    cluster = kmeans.predict(input_scaled)[0]

    cluster_labels = {
        0: "💎 Premium Customers — High income, high spending",
        1: "💰 Budget Shoppers — Low income, low spending",
        2: "🌐 Digital Buyers — Prefer online shopping",
        3: "😴 Dormant Customers — Inactive, needs re-engagement"
    }

    label = cluster_labels.get(cluster, f"Cluster {cluster}")
    st.success(f"Predicted Segment: {label}")