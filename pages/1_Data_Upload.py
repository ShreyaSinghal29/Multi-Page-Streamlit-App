import streamlit as st
import pandas as pd
import os

st.title("📂 Upload Dataset")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state['data'] = df  # Store in session state
    st.write("Dataset Preview:", df.head())

    # Save file to the data directory
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/dataset.csv", index=False)
    st.success("File uploaded and saved successfully!")
