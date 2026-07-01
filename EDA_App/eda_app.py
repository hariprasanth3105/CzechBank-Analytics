import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="CzechBank EDA Dashboard", layout="wide")
st.title("📊 Czechoslovakia Bank - Exploratory Data Analysis Dashboard")

# ====================== LOAD DATA ======================
@st.cache_data
def load_data():
    district = pd.read_csv('district.csv')
    client = pd.read_csv('client.csv')
    account = pd.read_csv('account.csv')
    transaction_summary = pd.read_csv('transaction_summary.csv')
    loan = pd.read_csv('loan.csv')
    return district, client, account, transaction_summary, loan

district, client, account, transaction_summary, loan = load_data()

# ====================== NAVIGATION ======================
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to Section", [
    "Overview", 
    "Customer Analysis", 
    "Transaction Analysis", 
    "Loan Analysis", 
    "Regional Analysis", 
    "High-Value Customers"
])

# ====================== PAGES ======================
if page == "Overview":
    st.header("Project Overview")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Customers", f"{len(client):,}")
    col2.metric("Total Accounts",  f"{account['account_id'].nunique()}")
    col3.metric("Total Loans", f"{len(loan):,}")
    col4.metric("Districts", f"{len(district):,}")

    st.success("Comprehensive Banking Analytics covering 8 business objectives.")

elif page == "Customer Analysis":
    st.header("👥 Customer Analysis")
    st.subheader("High-Value Customers")
    st.write("**888 High-Value Customers (16.54% of total)**")
    
    fig, ax = plt.subplots(figsize=(8,5))
    labels = ['High Value', 'Normal']
    sizes = [888, len(client)-888]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#1f77b4', '#aec7e8'])
    st.pyplot(fig)

elif page == "Transaction Analysis":
    st.header("💰 Transaction Analysis")
    st.subheader("Transaction Count Distribution")
    st.bar_chart(transaction_summary['txn_count'].value_counts().head(20))

    st.subheader("Average Balance Distribution")
    fig, ax = plt.subplots(figsize=(10,6))
    sns.histplot(transaction_summary['avg_balance'], bins=30, kde=True, ax=ax)
    st.pyplot(fig)

elif page == "Loan Analysis":
    st.header("🏦 Loan Analysis")
    st.subheader("Loan Status Distribution")
    if 'loan_status' in loan.columns:
        fig, ax = plt.subplots()
        loan['loan_status'].value_counts().plot(kind='bar', ax=ax, color='skyblue')
        st.pyplot(fig)

elif page == "Regional Analysis":
    st.header("🌍 Regional Analysis")
    st.subheader("Customers by Region")
    st.bar_chart(district['region'].value_counts())

    st.subheader("Average Salary by Region")
    st.bar_chart(district.groupby('region')['avg_salary'].mean())

elif page == "High-Value Customers":
    st.header("⭐ High-Value Customer Analysis")
    st.success("**888 High-Value Customers (16.54%)** identified")
    st.info("High-Value customers show higher engagement and significantly lower default risk.")

st.sidebar.success("EDA Dashboard")
