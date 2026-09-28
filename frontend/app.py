import streamlit as st
import requests

st.title("SuperKart Sales Prediction App")

# Input fields for product and store data
Product_Weight = st.number_input("Product Weight", min_value=0.0, value=12.66)

Product_Sugar_Content = st.selectbox(
    "Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"]
)

Product_Allocated_Area = st.number_input(
    "Product Allocated Area", min_value=0.0, value=0.05
)

Product_MRP = st.number_input(
    "Product MRP", min_value=0.0, value=150.0
)

Store_Size = st.selectbox(
    "Store Size", ["Small", "Medium", "High"]
)

Store_Location_City_Type = st.selectbox(
    "Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"]
)

Store_Type = st.selectbox(
    "Store Type",
    ["Supermarket Type1", "Supermarket Type2", "Departmental Store", "Food Mart"]
)

Product_Id_char = st.selectbox(
    "Product Category Code", ["FD", "DR", "NC"]
)

Store_Age_Years = st.number_input(
    "Store Age (Years)", min_value=0, value=10
)

Product_Type_Category = st.selectbox(
    "Product Type Category", ["Perishables", "Non Perishables"]
)

# Prepare input data
product_data = {
    "Product_Weight": Product_Weight,
    "Product_Sugar_Content": Product_Sugar_Content,
    "Product_Allocated_Area": Product_Allocated_Area,
    "Product_MRP": Product_MRP,
    "Store_Size": Store_Size,
    "Store_Location_City_Type": Store_Location_City_Type,
    "Store_Type": Store_Type,
    "Product_Id_char": Product_Id_char,
    "Store_Age_Years": Store_Age_Years,
    "Product_Type_Category": Product_Type_Category
}

# Replace with your actual HF space URL
API_URL = "https://vshah2-superkart-backend.hf.space/v1/predict"

if st.button("Predict", type='primary'):
    response = requests.post(API_URL, json=product_data)
    
    if response.status_code == 200:
        result = response.json()
        predicted_sales = result["Sales"]
        st.write(f"Predicted Product Store Sales Total: ₹{predicted_sales:.2f}")
    else:
        st.error("Error in API request")