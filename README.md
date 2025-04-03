
            Start editing…📌 Multi-Page Streamlit Machine Learning App## 📖 OverviewThis project is a multi-page Streamlit application for data preprocessing, model training, and evaluation. It allows users to:✅ Upload a dataset✅ Perform data preprocessing✅ Train a machine learning model✅ Evaluate model performance✅ Make predictions using the trained model## 🚀 FeaturesUser-friendly UI with StreamlitMulti-page navigationHandles missing values during preprocessingTrains a machine learning model (Random Forest by default)Evaluates model accuracyAllows predictions using the trained model## 📂 Project Structurestreamlit_ml_app/
│── main.py                # Main entry point for the Streamlit app
│── pages/
│   ├── 1_Data_Upload.py    # Page to upload data
│   ├── 2_Data_Preprocessing.py # Page for preprocessing steps
│   ├── 3_Model_Training.py # Page for training ML model
│   ├── 4_Model_Evaluation.py # Page for model evaluation
│   ├── 5_Prediction.py     # Page to make predictions
│── data/                  # Directory to store uploaded files
│── models/                # Directory to save trained models
└── requirements.txt        # Dependencies## 🔧 Installation &amp; Setup### 1️⃣ Clone the Repositorygit clone https://github.com/ShreyaSinghal29/Multi-Page-Streamlit-App.git
cd Multi-Page-Streamlit-App### 2️⃣ Install Dependenciespip install -r requirements.txt### 3️⃣ Run the Streamlit Appstreamlit run main.py## 🛠 Usage Guide### Step 1: Upload DatasetNavigate to the "Upload Dataset" page and upload a CSV file.### Step 2: Data PreprocessingHandle missing values and preprocess the dataset.### Step 3: Train ModelSelect the target column and train a Random Forest Classifier.### Step 4: Evaluate ModelView the model accuracy and performance metrics.### Step 5: Make PredictionsInput new data and get predictions from the trained model.## 🚀 Deployment (Optional)### Deploying on Streamlit CloudPush your project to GitHub.Go to Streamlit Cloud.Click on "New App" and connect your GitHub repository.Select main.py as the entry point and deploy.## 🤝 ContributingPull requests are welcome! Feel free to open an issue or suggest improvements.## 📜 LicenseThis project is open-source under the MIT License.### 🔗 Author: [Shreya Singhal](https://github.com/ShreyaSinghal29" disabled="false)
