import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder  # Import LabelEncoder
import pickle
import os

st.title("🚀 Train a Model")

if 'processed_data' in st.session_state:
    df = st.session_state['processed_data']

    target = st.selectbox("Select Target Column", df.columns)
    features = [col for col in df.columns if col != target]

    X = df[features]
    y = df[target]

    # ✅ Step 1: Convert Categorical Columns to Numeric
    for col in X.columns:
        if X[col].dtype == 'object':  # Check if column is categorical
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col])  # Convert to numbers

    # ✅ Step 2: Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # ✅ Step 3: Train the Model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    # ✅ Step 4: Save Model
    os.makedirs("models", exist_ok=True)
    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)

    st.success("✅ Model Trained and Saved Successfully!")
else:
    st.warning("⚠️ Please preprocess the data first.")
