import streamlit as st
import pandas as pd
import joblib
import urllib
from sqlalchemy import create_engine

# ====================== SQL CONNECTION ======================
@st.cache_resource
def get_engine():
    server = 'LAPTOP-6PATUP9M\\SQLEXPRESS'
    database = 'CzechBankDB'
    params = urllib.parse.quote_plus(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"Trusted_Connection=yes;"
    )
    return create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

engine = get_engine()

# Load district table
@st.cache_data
def load_district():
    return pd.read_sql("SELECT * FROM district", engine)

district = load_district()

# ====================== APP STARTS HERE ======================
st.set_page_config(page_title="Loan Default Risk Predictor", layout="wide")
st.title("🏦 Loan Default Risk Predictor")
st.markdown("### Predict the risk of loan default")

# District lookup
district_lookup = district[['district_id', 'district_name', 'region', 'population', 
                           'avg_salary', 'unemployment_rate_1995', 'unemployment_rate_1996']]

col1, col2 = st.columns(2)

with col1:
    district_id = st.selectbox("District ID", options=district_lookup['district_id'].unique())
    district_info = district_lookup[district_lookup['district_id'] == district_id].iloc[0]
    
    loan_amount = st.number_input("Loan Amount", value=150000, min_value=10000)
    monthly_payments = st.number_input("Monthly Payments", value=4800, min_value=1000)
    avg_balance = st.number_input("Average Balance", value=18500, min_value=0)
    txn_count = st.number_input("Transaction Count", value=245, min_value=0)
    age = st.number_input("Customer Age", value=34, min_value=18)

with col2:
    st.write(f"**District:** {district_info['district_name']}")
    st.write(f"**Region:** {district_info['region']}")
    
    credit_debit_ratio = st.slider("Credit/Debit Ratio", 0.0, 1.5, 0.65)
    payment_to_income_ratio = st.slider("Payment to Income Ratio", 0.0, 1.0, 0.49)
    balance_to_loan_ratio = st.slider("Balance to Loan Ratio", 0.0, 1.0, 0.12)

if st.button("Predict Risk", type="primary"):
    input_data = pd.DataFrame({
        'loan_amount': [loan_amount],
        'loan_duration': [36],
        'monthly_payments': [monthly_payments],
        'age': [age],
        'population': [district_info['population']],
        'avg_salary': [district_info['avg_salary']],
        'unemployment_rate_1995': [district_info['unemployment_rate_1995']],
        'unemployment_rate_1996': [district_info['unemployment_rate_1996']],
        'avg_balance': [avg_balance],
        'txn_count': [txn_count],
        'avg_txn_amount': [6200],
        'credit_debit_ratio': [credit_debit_ratio],
        'loan_to_income_ratio': [loan_amount / district_info['avg_salary']],
        'payment_to_income_ratio': [payment_to_income_ratio],
        'balance_to_loan_ratio': [balance_to_loan_ratio],
        'frequency_POPLATEK PO OBRATU': [0],
        'frequency_POPLATEK TYDNE': [0],
        'gender_Male': [1],
        'region_central Bohemia': [1 if district_info['region'] == 'central Bohemia' else 0],
        'region_east Bohemia': [1 if district_info['region'] == 'east Bohemia' else 0],
        'region_north Bohemia': [1 if district_info['region'] == 'north Bohemia' else 0],
        'region_north Moravia': [1 if district_info['region'] == 'north Moravia' else 0],
        'region_south Bohemia': [1 if district_info['region'] == 'south Bohemia' else 0],
        'region_south Moravia': [1 if district_info['region'] == 'south Moravia' else 0],
        'region_west Bohemia': [1 if district_info['region'] == 'west Bohemia' else 0],
        'district_name_encoded': [0.085]
    })
    
    model = joblib.load('loan_default_model.pkl')
    prob = model.predict_proba(input_data)[:, 1][0]
    risk = "🔴 HIGH RISK" if prob >= 0.3 else "🟢 LOW RISK"
    
    st.success(f"Default Probability: **{prob:.2%}**")
    st.markdown(f"### Risk Level: **{risk}**")

st.info("Threshold = 0.3 | Higher probability = Higher default risk")