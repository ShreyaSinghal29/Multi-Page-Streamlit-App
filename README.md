# 📌 Multi-Page Streamlit Machine Learning App

## 📖 Overview
This project is a **multi-page Streamlit application** for **data preprocessing, model training, and evaluation**. It allows users to:

✅ Upload a dataset  
✅ Perform data preprocessing  
✅ Train a machine learning model  
✅ Evaluate model performance  
✅ Make predictions using the trained model  

## 🚀 Features
- **User-friendly UI** with Streamlit
- **Multi-page navigation**
- **Handles missing values** during preprocessing
- **Trains a machine learning model** (Random Forest by default)
- **Evaluates model accuracy**
- **Allows predictions** using the trained model

## 📂 Project Structure
```bash
streamlit_ml_app/
│── main.py                # Main entry point for the Streamlit app
│── pages/
│   ├── 1_Data_Upload.py    # Page to upload data
│   ├── 2_Data_Preprocessing.py # Page for preprocessing steps
│   ├── 3_Model_Training.py # Page for training ML model
│   ├── 4_Model_Evaluation.py # Page for model evaluation
│   ├── 5_Prediction.py     # Page to make predictions
│── data/                  # Directory to store uploaded files
│── models/                # Directory to save trained models
└── requirements.txt        # Dependencies
```

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/ShreyaSinghal29/Multi-Page-Streamlit-App.git
cd Multi-Page-Streamlit-App
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App
```sh
streamlit run main.py
```

## 🛠 Usage Guide
### **Step 1: Upload Dataset**
- Navigate to the "Upload Dataset" page and upload a CSV file.

### **Step 2: Data Preprocessing**
- Handle missing values and preprocess the dataset.

### **Step 3: Train Model**
- Select the target column and train a **Random Forest Classifier**.

### **Step 4: Evaluate Model**
- View the model accuracy and performance metrics.

### **Step 5: Make Predictions**
- Input new data and get predictions from the trained model.

## 🚀 Deployment (Optional)
### **Deploying on Streamlit Cloud**
1. Push your project to **GitHub**.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Click on "New App" and connect your GitHub repository.
4. Select `main.py` as the entry point and deploy.

## 🤝 Contributing
Pull requests are welcome! Feel free to open an issue or suggest improvements.

## 📜 License
This project is **open-source** under the **MIT License**.

---

### 🔗 **Author**: [Shreya Singhal](https://github.com/ShreyaSinghal29)

