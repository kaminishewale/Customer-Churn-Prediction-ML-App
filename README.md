# 📊 Customer Churn Prediction – Machine Learning Web App

## 📌 Project Overview

This project predicts whether a telecom customer is likely to churn using Machine Learning.  

The project includes:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Logistic Regression & Random Forest models
- Model Evaluation (Accuracy, Precision, Recall, F1-score)
- Streamlit Web Application for real-time prediction

---

## 📂 Dataset Information

- Dataset: Telco Customer Churn Dataset
- Records: 7032 customers
- Features: 20 cleaned features
- Target Variable: `Churn Value` (0 = Stay, 1 = Churn)

---

## ⚙️ Machine Learning Models Used

### 1️⃣ Logistic Regression
- Accuracy: **81.23%**
- Recall (Churn Class): 58%
- Best performing model

### 2️⃣ Random Forest
- Accuracy: 79.60%

Logistic Regression performed better on test data.

---

## 📊 Model Evaluation

Confusion Matrix (Logistic Regression):

- 915 customers correctly predicted as non-churn
- 228 customers correctly predicted as churn
- 81% overall accuracy

---

## 💡 Key Business Insights

- Customers with month-to-month contracts have higher churn rate.
- Higher monthly charges increase churn probability.
- Customers with shorter tenure are more likely to churn.

This model helps telecom companies identify at-risk customers and improve retention strategies.

---

## 🌐 Streamlit Web Application

The project includes an interactive web app built using Streamlit.

Features:
- User input for customer details
- Real-time churn prediction
- Churn probability percentage display

---

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib
