# Customer Churn Prediction [🔗](https://customer-churn-prediction-shk.streamlit.app/)
A machine learning project to predict customer churn using historical data, with complete preprocessing, modeling, and feature analysis in a single notebook.

## 📌 Objective
Predict whether a customer will discontinue a subscription-based service based on their historical data.

We analyze factors like:
- Usage patterns
- Demographic details
- Subscription duration
- Other important features

The project aims to:
- Build an accurate churn prediction model.
- Identify the most significant factors influencing customer churn.

---
## Streamlit
I have done a beautiful and lightweight **Streamlit web application** for predicting **customer churn** probability using a machine learning model.  

---

## 🚀 Features
- Predicts if a customer will **churn** or **stay**.
- Displays **churn probability (%)** using an attractive **speedometer (gauge meter)**.
- **Custom header** with title and quick access buttons.
- **Beautiful light theme** with dynamic CSS styling.
- **Footer fixed** at the bottom showing copyright.
- **Responsive layout** using Streamlit and Plotly.

---
## 🚀 Steps to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/BSHK57/customer-churn-prediction.git
   cd customer-churn-prediction

2. **Install Required Libraries**
   ```bash
   pip install -r requirements.txt
   ```

3. **Open the Notebook**
   - Launch Jupyter Notebook or Jupyter Lab.
   - Open `Customer_Churn_Prediction.ipynb`.

4. **Run All Cells**
   - The notebook will guide you through:
     - Data loading
     - Data preprocessing (handling missing values, encoding, scaling)
     - Exploratory Data Analysis (EDA)
     - Model training
     - Model evaluation
     - Feature importance analysis

5. **Run the app**:
   ```bash
   streamlit run Strealit.py
   ```

---

## 📂 Project Structure

```
customer-churn-prediction/
│
├── customer_data.csv       # Dataset (sample or provided separately)
│
├── Customer_Churn_Prediction.ipynb  # Main notebook (all code + output)
│
├── EDA.ipynb
│
├── streamlit run Strealit.py    # Streamlit Application
│
├── README.md                   # Project documentation
│
└── requirements.txt            # Python libraries needed
```
---

## 📎 Links
- [🔗 GitHub Repository](https://github.com/BSHK57/customer-churn-prediction)
- [📄 Dataset Source](https://www.kaggle.com/datasets/shantanudhakadd/bank-customer-churn-prediction/data)
- [Streamlit](https://customer-churn-prediction-shk.streamlit.app/)
__Try to restart if it already dead__

---
---

## 📈 Model Overview

- **Model Used:** Random Forest Classifier
- **Key Steps:**
  - Imputed missing values
  - Encoded categorical variables
  - Scaled numerical features
  - Trained Random Forest model
  - Evaluated using accuracy, confusion matrix, and classification report
  - Analyzed feature importance

---

## ✅ Highlights
- Single, clean, well-structured Jupyter Notebook.
- Easy to follow with comments and section headers.
- Includes basic Exploratory Data Analysis (EDA).
- Focused on real-world practical churn prediction.
---
