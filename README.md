# CzechBank Analytics - Banking Insights & Default Prediction

A comprehensive data analytics solution for **Czechoslovakia Bank** built as part of the AnalytixLabs Internship Program.

---

## 🎯 Project Objective

To analyze banking data and build actionable insights across customer behavior, loan risk, regional performance, and profitability to support data-driven decision making.

---

## 📊 Key Features

- **Exploratory Data Analysis** on 8 interconnected banking tables
- **High-Value Customer Identification** using RFM-inspired scoring
- **Loan Default Prediction Model** (XGBoost) with 60% recall at optimal threshold
- **Interactive Streamlit Web App** for real-time loan risk prediction
- **RFM & Cohort Analysis** for customer segmentation
- **Strategic Business Recommendations**

---

## 🛠️ Tech Stack

- **Python** (Pandas, Scikit-learn, XGBoost)
- **SQL Server** (Data storage & querying)
- **Streamlit** (Interactive Web Dashboard)
- **Matplotlib & Seaborn** (Visualizations)
- **Joblib** (Model & Scaler serialization)

---

## 📁 Project Structure

CzechBank-Analytics/

├── EDA_App/                    # EDA Streamlit Web Application

│   ├── eda_app.py

│   ├── account.csv

│   ├── client.csv

│   ├── district.csv

│   ├── loan.csv

│   └── transaction_summary.csv

├── CzechBank_EDA.ipynb            # Exploratory Data Analysis

├── CzechBank_FinalML.ipynb        # Machine Learning Models

├── loanrisk_app.py                # Streamlit Web Application

├── loan_default_model.pkl         # Trained XGBoost Model

├── requirements.txt

└── README.md




**Streamlit App**:
[CzechBank Loan Risk Predictor](https://czechbank-analytics-brkgdg6myinywaays9vrcf.streamlit.app)
[EDA Web Application](https://czechbank-analytics-b4rlfwn9teeb25pietkafx.streamlit.app)
---

## 📈 Key Insights

- Identified **16.54% High-Value Customers** with significantly lower risk
- Developed a **Loan Default Model** with **60% Recall** at threshold 0.3
- Discovered strong regional variations in customer quality and volume
- Found major cross-selling opportunity among single-product customers (73.6%)

---

## 🏆 Business Recommendations

- Prioritize retention of High-Value customers
- Implement targeted cross-selling for single-product customers
- Use balance and credit/debit ratio as key risk indicators
- Focus growth in high-potential, low-risk districts

---

## 🛠️ How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/hariprasanth3105/CzechBank-Analytics.git

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run loanrisk_app.py
streamlit run EDA_App/eda_app.py
