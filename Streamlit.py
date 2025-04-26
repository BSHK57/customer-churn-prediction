import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# Load model and encoders
loaded_model = joblib.load('customer_churn_model.pkl')
loaded_les = joblib.load('label_encoders.pkl')

# Set Streamlit page config
st.set_page_config(page_title="Customer Churn Prediction", page_icon="✨", layout="centered", initial_sidebar_state="auto")

# Custom CSS for Main Header, Buttons, Footer
st.markdown(
    """
    <style>
    body {
        background-color: #f9f9f9;
        margin: 0;
        padding: 0;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
    }
    .main {
        flex: 1;
    }
    .main-header {
        text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .main-header h1 {
        font-size: 42px;
        color: #4a4a4a;
        font-weight: bold;
    }
    .links {
        text-align: center;
        margin-bottom: 30px;
    }
    .links a {
        text-decoration: none;
        color: white;
        background-color: #007acc;
        padding: 8px 16px;
        border-radius: 5px;
        margin: 10px;
        font-size: 16px;
        transition: 0.3s;
    }
    .links a:hover {
        background-color: #005f99;
    }
    .prediction {
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        padding-top: 20px;
    }
    footer {
        text-align: center;
        font-size: 14px;
        color: #888;
        padding: 20px 10px;
        margin-top: auto;
        background: transparent;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# MAIN HEADER
st.markdown('<header class="main-header"><h1>✨ Customer Churn Prediction</h1></header>', unsafe_allow_html=True)

# Buttons under header
st.markdown(
    """
    <div class="links">
        <a href="https://github.com/BSHK57/customer-churn-prediction" target="_blank">🔗 GitHub Repository</a>
        <a href="https://www.kaggle.com/datasets/shantanudhakadd/bank-customer-churn-prediction/data" target="_blank">📄 Dataset Source</a>
    </div>
    """,
    unsafe_allow_html=True
)

# --- FORM section starts ---
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        CreditScore = st.number_input('Credit Score', min_value=300, max_value=900, value=600)
        Geography = st.selectbox('Geography', options=loaded_les['Geography'].classes_.tolist())
        Gender = st.selectbox('Gender', options=loaded_les['Gender'].classes_.tolist())
        Age = st.slider('Age', min_value=18, max_value=100, value=40)
        Tenure = st.slider('Tenure (Years)', min_value=0, max_value=10, value=3)
        
    with col2:
        Balance = st.number_input('Balance', min_value=0.0, value=60000.0, step=1000.0)
        NumOfProducts = st.selectbox('Number of Products', options=[1, 2, 3, 4])
        HasCrCard = st.radio('Has Credit Card?', options=[0, 1])
        IsActiveMember = st.radio('Is Active Member?', options=[0, 1])
        EstimatedSalary = st.number_input('Estimated Salary', min_value=0.0, value=50000.0, step=1000.0)
    
    submit_button = st.form_submit_button(label="Predict")

# --- FORM section ends ---

# When form is submitted
if submit_button:
    input_data = {
        'CreditScore': CreditScore,
        'Geography': Geography,
        'Gender': Gender,
        'Age': Age,
        'Tenure': Tenure,
        'Balance': Balance,
        'NumOfProducts': NumOfProducts,
        'HasCrCard': HasCrCard,
        'IsActiveMember': IsActiveMember,
        'EstimatedSalary': EstimatedSalary
    }
    
    feature_names = ['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 
                     'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']
    
    input_df = pd.DataFrame([input_data], columns=feature_names)
    
    # Encoding categorical variables
    input_df['Gender'] = loaded_les['Gender'].transform([input_df.loc[0, 'Gender']])[0]
    input_df['Geography'] = loaded_les['Geography'].transform([input_df.loc[0, 'Geography']])[0]
    
    prediction = loaded_model.predict(input_df)
    prediction_proba = loaded_model.predict_proba(input_df)[0][1]  # Probability of churn
    churn_probability = round(prediction_proba * 100, 2)

    # Display result
    if prediction[0] == 1:
        st.markdown('<div class="prediction" style="color: red;">⚠️ The customer is likely to churn.</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="prediction" style="color: green;">✅ The customer is likely to stay.</div>', unsafe_allow_html=True)

    # Display speedometer
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=churn_probability,
        title={'text': "Churn Probability (%)", 'font': {'size': 24}},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 30], 'color': "#00cc96"},
                {'range': [30, 70], 'color': "#ffa600"},
                {'range': [70, 100], 'color': "#ef553b"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': churn_probability
            }
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

# MAIN FOOTER
st.markdown(
    """
    <footer>
        All Rights Reserved © Sai Hari Krishna, 2025
    </footer>
    """,
    unsafe_allow_html=True
)