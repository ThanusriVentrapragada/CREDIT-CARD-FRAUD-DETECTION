# 💳 Credit Card Fraud Detection

A machine learning web application that detects potentially fraudulent credit card transactions using **Logistic Regression** and provides a probability-based prediction through a **Streamlit** interface.

## 🚀 Live Demo

[Open the Live Streamlit App](https://credit-card-fraud-detection-wnrqyrhrvsvtnkbdytny46.streamlit.app/)

## 📂 GitHub Repository

[View the Source Code](https://github.com/ThanusriVentrapragada/CREDIT-CARD-FRAUD-DETECTION)

## 📌 Project Overview

Credit card fraud is a major challenge in digital payment systems. Since fraudulent transactions are much less frequent than legitimate transactions, detecting them accurately requires an appropriate machine learning approach.

This project uses the Credit Card Fraud Detection dataset to train a Logistic Regression model that classifies transactions as:

* **Legitimate**
* **Fraudulent**

The trained model is integrated into a Streamlit application where users can enter transaction details and receive a prediction along with the estimated fraud probability.

## 🎯 Objectives

* Detect fraudulent credit card transactions using machine learning.
* Apply data preprocessing and feature scaling.
* Train a Logistic Regression classification model.
* Evaluate the model using multiple classification metrics.
* Build an interactive Streamlit web application.
* Deploy the application online for demonstration.

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Matplotlib**
* **Joblib**
* **Streamlit**
* **Git & GitHub**

## 🧠 Machine Learning Workflow

```text
Credit Card Transaction Dataset
              ↓
        Data Preprocessing
              ↓
        Feature Scaling
              ↓
       Train/Test Split
              ↓
      Logistic Regression
              ↓
       Model Evaluation
              ↓
        Save Model
              ↓
       Streamlit Web App
              ↓
     Fraud / Legitimate
```

## 📊 Dataset

The project uses the **Credit Card Fraud Detection dataset** containing transactions made by European cardholders.

The dataset contains:

* `Time` — Time elapsed between transactions.
* `V1` to `V28` — PCA-transformed features.
* `Amount` — Transaction amount.
* `Class` — Target variable.

The target variable is:

```text
0 → Legitimate Transaction
1 → Fraudulent Transaction
```

The original dataset is approximately **151 MB**, so it is intentionally not stored in this GitHub repository.

## 🤖 Machine Learning Model

### Logistic Regression

Logistic Regression is used as the classification algorithm because it is suitable for binary classification and provides probability estimates for predictions.

The model follows this process:

```text
Input Transaction
       ↓
StandardScaler
       ↓
Logistic Regression
       ↓
Prediction Probability
       ↓
Fraud / Legitimate
```

## 📈 Model Evaluation

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Confusion Matrix
* ROC Curve
* Precision-Recall Curve

For fraud detection, **Precision and Recall** are particularly important because fraudulent transactions represent a very small portion of the overall dataset.

## 💻 Streamlit Application

The web application provides:

* Transaction statistics
* Fraud vs legitimate transaction overview
* Model performance metrics
* Confusion matrix
* ROC curve
* Precision-Recall curve
* Transaction prediction
* Fraud probability

## 📁 Project Structure

```text
CREDIT-CARD-FRAUD-DETECTION/
│
├── app.py
├── train_model.py
├── fraud_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
├── .gitignore
│
└── data/
    └── creditcard.csv
```

> The dataset is kept locally and excluded from GitHub because of its large file size.

## ⚙️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/ThanusriVentrapragada/CREDIT-CARD-FRAUD-DETECTION.git
cd CREDIT-CARD-FRAUD-DETECTION
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add the dataset

Download the Credit Card Fraud Detection dataset and place:

```text
creditcard.csv
```

inside:

```text
data/
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open locally at:

```text
http://localhost:8501
```

## 🔮 Future Improvements

Some possible improvements for future versions include:

* Handling class imbalance using SMOTE or other techniques.
* Comparing Logistic Regression with Random Forest, XGBoost, and other classifiers.
* Adding threshold tuning for fraud detection.
* Improving the transaction input interface.
* Adding model explainability using SHAP or similar techniques.
* Monitoring model performance on new transaction data.

## 👩‍💻 Author

**Thanusri Ventrapragada**

B.Tech — Electronics and Communication Engineering

## ⭐ Project Highlights

* End-to-end machine learning project
* Binary classification for fraud detection
* Feature preprocessing and scaling
* Model evaluation using multiple metrics
* Interactive Streamlit application
* GitHub version control
* Cloud deployment
