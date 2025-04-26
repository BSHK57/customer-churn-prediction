# Customer Churn Prediction
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

## 🚀 Steps to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/BSHK57/customer-churn-prediction.git
   cd customer-churn-prediction
Awesome — you want the **code inside one Jupyter Notebook** and a **separate clean `README.md`**.  
Here’s the `README.md` you can directly use for your repository:

---

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
├── README.md                   # Project documentation
│
└── requirements.txt            # Python libraries needed
```

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