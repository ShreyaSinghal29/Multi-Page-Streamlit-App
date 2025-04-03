import streamlit as st
import pandas as pd
import pickle
import os  # ✅ Make sure os is imported

st.title("📊 Model Evaluation")

if os.path.exists("models/model.pkl"):  # ✅ os is now defined
    df = pd.read_csv("data/processed_data.csv")
    with open("models/model.pkl", "rb") as f:
        model = pickle.load(f)

    target = st.selectbox("Select Target Column", df.columns)
    features = [col for col in df.columns if col != target]

    X = df[features]
    y = df[target]

    y_pred = model.predict(X)

    from sklearn.metrics import accuracy_score
    accuracy = accuracy_score(y, y_pred)
    st.write(f"Model Accuracy: {accuracy:.2f}")

else:
    st.warning("Please train the model first.")
