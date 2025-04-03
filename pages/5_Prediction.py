import os  # ✅ Fix the NameError
import streamlit as st
import pandas as pd
import pickle

st.title("🔮 Make Predictions")

if os.path.exists("models/model.pkl"):  # ✅ os is now recognized
    with open("models/model.pkl", "rb") as f:
        model = pickle.load(f)

    df = pd.read_csv("data/processed_data.csv")
    input_data = {}

    for col in df.columns[:-1]:  # Exclude target column
        input_data[col] = st.number_input(f"Enter {col}", value=df[col].mean())

    input_df = pd.DataFrame([input_data])

    if st.button("Predict"):
        prediction = model.predict(input_df)
        st.success(f"Predicted Output: {prediction[0]}")
else:
    st.warning("Please train the model first.")
