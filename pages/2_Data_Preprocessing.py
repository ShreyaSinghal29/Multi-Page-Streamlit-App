import streamlit as st
import pandas as pd

st.title("🛠 Data Preprocessing")

if 'data' in st.session_state:
    df = st.session_state['data']
    st.write("Original Data:", df.head())

    # Handling missing values
    if st.checkbox("Fill Missing Values"):
        df.fillna(df.mean(), inplace=True)
        st.write("Updated Data:", df.head())

    st.session_state['processed_data'] = df
    df.to_csv("data/processed_data.csv", index=False)
    st.success("Data Preprocessed and Saved!")
else:
    st.warning("Please upload a dataset first.")
