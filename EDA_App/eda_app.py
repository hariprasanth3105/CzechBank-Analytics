import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="CzechBank EDA Dashboard", layout="wide")
st.title("📊 Czechoslovakia Bank - Exploratory Data Analysis Dashboard")

# ====================== LOAD DATA FROM CSV ======================
@st.cache_data
def load_data():
    district = pd.read_csv('district.csv')
    client = pd.read_csv('client.csv')
    account = pd.read_csv('account.csv')
    transaction = pd.read_csv('transaction.csv')
    loan = pd.read_csv('loan.csv')
    return district, client, account, transaction, loan

district, client, account, transaction, loan = load_data()

# ====================== SIDEBAR ======================
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
    col1, col2, col3, col4,col5 = st.columns(5)
    col1.metric("Total Client", f"{len(client):,}")
    col2.metric("Total Account", f"{account['account_id'].nunique()}")
    col3.metric("Total Transactions", f"{len(transaction):,}")
    col4.metric("Total Loans", f"{len(loan):,}")
    col5.metric("Districts", f"{len(district):,}")


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

    st.subheader("Product Holding")
    st.bar_chart({"1 Product": 73.6, "2 Products": 23.0, "3 Products": 3.4})

elif page == "Transaction Analysis":
    st.header("💰 Transaction Analysis")
    st.subheader("Transaction Type Distribution")
    if 'type' in transaction.columns:
        st.bar_chart(transaction['type'].value_counts())

    st.subheader("Balance Distribution")
    fig, ax = plt.subplots(figsize=(10,6))
    sns.histplot(transaction['balance'].dropna(), bins=50, kde=True, ax=ax)
    st.pyplot(fig)

elif page == "Loan Analysis":
    st.header("🏦 Loan Analysis")
    st.subheader("Loan Status Distribution")
    if 'loan_status' in loan.columns:
        fig, ax = plt.subplots()
        loan['loan_status'].value_counts().plot(kind='bar', ax=ax, color='skyblue')
        st.pyplot(fig)

    st.subheader("Problematic Loans")
    st.write("**11.14%** of loans are problematic (Status B & D)")

elif page == "Regional Analysis":
    st.header("🌍 Regional Analysis")
    st.subheader("Customers by Region")
    if 'region' in district.columns:
        st.bar_chart(district['region'].value_counts())

    st.subheader("Average Salary by Region")
    if 'region' in district.columns and 'avg_salary' in district.columns:
        avg_salary = district.groupby('region')['avg_salary'].mean()
        st.bar_chart(avg_salary)

elif page == "High-Value Customers":
    st.header("⭐ High-Value Customer Analysis")
    st.success("**888 High-Value Customers (16.54%)** identified")
    st.write("""
    - Higher transaction volume and balance
    - Significantly lower default risk
    - Better product adoption
    """)
    st.info("Focus retention and cross-selling on this segment for maximum ROI.")

st.sidebar.info("EDA Dashboard")
