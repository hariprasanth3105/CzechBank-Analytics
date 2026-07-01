import streamlit as st
import pandas as pd
import joblib




# ====================== APP STARTS HERE ======================
st.set_page_config(page_title="Loan Default Risk Predictor", layout="wide")
st.title("🏦 Loan Default Risk Predictor")
st.markdown("### Predict the risk of loan default")

# Static District Data

district_data = {
'district_id': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 13: 14, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19, 19: 20, 20: 21, 21: 22, 22: 23, 23: 24, 24: 25, 25: 26, 26: 27, 27: 28, 28: 29, 29: 30, 30: 31, 31: 32, 32: 33, 33: 34, 34: 35, 35: 36, 36: 37, 37: 38, 38: 39, 39: 40, 40: 41, 41: 42, 42: 43, 43: 44, 44: 45, 45: 46, 46: 47, 47: 48, 48: 49, 49: 50, 50: 51, 51: 52, 52: 53, 53: 54, 54: 55, 55: 56, 56: 57, 57: 58, 58: 59, 59: 60, 60: 61, 61: 62, 62: 63, 63: 64, 64: 65, 65: 66, 66: 67, 67: 68, 68: 69, 69: 70, 70: 71, 71: 72, 72: 73, 73: 74, 74: 75, 75: 76, 76: 77}, 
'district_name': {0: 'Hl.m. Praha', 1: 'Benesov', 2: 'Beroun', 3: 'Kladno', 4: 'Kolin', 5: 'Kutna Hora', 6: 'Melnik', 7: 'Mlada Boleslav', 8: 'Nymburk', 9: 'Praha - vychod', 10: 'Praha - zapad', 11: 'Pribram', 12: 'Rakovnik', 13: 'Ceske Budejovice', 14: 'Cesky Krumlov', 15: 'Jindrichuv Hradec', 16: 'Pelhrimov', 17: 'Pisek', 18: 'Prachatice', 19: 'Strakonice', 20: 'Tabor', 21: 'Domazlice', 22: 'Cheb', 23: 'Karlovy Vary', 24: 'Klatovy', 25: 'Plzen - mesto', 26: 'Plzen - jih', 27: 'Plzen - sever', 28: 'Rokycany', 29: 'Sokolov', 30: 'Tachov', 31: 'Ceska Lipa', 32: 'Decin', 33: 'Chomutov', 34: 'Jablonec n. Nisou', 35: 'Liberec', 36: 'Litomerice', 37: 'Louny', 38: 'Most', 39: 'Teplice', 40: 'Usti nad Labem', 41: 'Havlickuv Brod', 42: 'Hradec Kralove', 43: 'Chrudim', 44: 'Jicin', 45: 'Nachod', 46: 'Pardubice', 47: 'Rychnov nad Kneznou', 48: 'Semily', 49: 'Svitavy', 50: 'Trutnov', 51: 'Usti nad Orlici', 52: 'Blansko', 53: 'Brno - mesto', 54: 'Brno - venkov', 55: 'Breclav', 56: 'Hodonin', 57: 'Jihlava', 58: 'Kromeriz', 59: 'Prostejov', 60: 'Trebic', 61: 'Uherske Hradiste', 62: 'Vyskov', 63: 'Zlin', 64: 'Znojmo', 65: 'Zdar nad Sazavou', 66: 'Bruntal', 67: 'Frydek - Mistek', 68: 'Jesenik', 69: 'Karvina', 70: 'Novy Jicin', 71: 'Olomouc', 72: 'Opava', 73: 'Ostrava - mesto', 74: 'Prerov', 75: 'Sumperk', 76: 'Vsetin'},
'region': {0: 'Prague', 1: 'central Bohemia', 2: 'central Bohemia', 3: 'central Bohemia', 4: 'central Bohemia', 5: 'central Bohemia', 6: 'central Bohemia', 7: 'central Bohemia', 8: 'central Bohemia', 9: 'central Bohemia', 10: 'central Bohemia', 11: 'central Bohemia', 12: 'central Bohemia', 13: 'south Bohemia', 14: 'south Bohemia', 15: 'south Bohemia', 16: 'south Bohemia', 17: 'south Bohemia', 18: 'south Bohemia', 19: 'south Bohemia', 20: 'south Bohemia', 21: 'west Bohemia', 22: 'west Bohemia', 23: 'west Bohemia', 24: 'west Bohemia', 25: 'west Bohemia', 26: 'west Bohemia', 27: 'west Bohemia', 28: 'west Bohemia', 29: 'west Bohemia', 30: 'west Bohemia', 31: 'north Bohemia', 32: 'north Bohemia', 33: 'north Bohemia', 34: 'north Bohemia', 35: 'north Bohemia', 36: 'north Bohemia', 37: 'north Bohemia', 38: 'north Bohemia', 39: 'north Bohemia', 40: 'north Bohemia', 41: 'east Bohemia', 42: 'east Bohemia', 43: 'east Bohemia', 44: 'east Bohemia', 45: 'east Bohemia', 46: 'east Bohemia', 47: 'east Bohemia', 48: 'east Bohemia', 49: 'east Bohemia', 50: 'east Bohemia', 51: 'east Bohemia', 52: 'south Moravia', 53: 'south Moravia', 54: 'south Moravia', 55: 'south Moravia', 56: 'south Moravia', 57: 'south Moravia', 58: 'south Moravia', 59: 'south Moravia', 60: 'south Moravia', 61: 'south Moravia', 62: 'south Moravia', 63: 'south Moravia', 64: 'south Moravia', 65: 'south Moravia', 66: 'north Moravia', 67: 'north Moravia', 68: 'north Moravia', 69: 'north Moravia', 70: 'north Moravia', 71: 'north Moravia', 72: 'north Moravia', 73: 'north Moravia', 74: 'north Moravia', 75: 'north Moravia', 76: 'north Moravia'},
'population': {0: 1204953, 1: 88884, 2: 75232, 3: 149893, 4: 95616, 5: 77963, 6: 94725, 7: 112065, 8: 81344, 9: 92084, 10: 75637, 11: 107870, 12: 53921, 13: 177686, 14: 58796, 15: 93931, 16: 74062, 17: 70699, 18: 51428, 19: 70646, 20: 103347, 21: 58400, 22: 87419, 23: 122603, 24: 88757, 25: 170449, 26: 67298, 27: 72541, 28: 45714, 29: 94812, 30: 51313, 31: 105058, 32: 133777, 33: 125236, 34: 88768, 35: 159617, 36: 114006, 37: 85852, 38: 119895, 39: 128118, 40: 118650, 41: 95907, 42: 161854, 43: 105606, 44: 77917, 45: 112709, 46: 162580, 47: 78955, 48: 75685, 49: 102609, 50: 121947, 51: 139012, 52: 107911, 53: 387570, 54: 157042, 55: 124605, 56: 161954, 57: 109164, 58: 108871, 59: 110643, 60: 117897, 61: 145688, 62: 86513, 63: 197099, 64: 114200, 65: 125832, 66: 106054, 67: 228848, 68: 42821, 69: 285387, 70: 161227, 71: 226122, 72: 182027, 73: 323870, 74: 138032, 75: 127369, 76: 148545},
'avg_salary': {0: 12541, 1: 8507, 2: 8980, 3: 9753, 4: 9307, 5: 8546, 6: 9920, 7: 11277, 8: 8899, 9: 10124, 10: 9622, 11: 8754, 12: 8598, 13: 10045, 14: 9045, 15: 8427, 16: 8114, 17: 8968, 18: 8402, 19: 8547, 20: 9104, 21: 8620, 22: 8624, 23: 8991, 24: 8554, 25: 10787, 26: 8561, 27: 8594, 28: 8843, 29: 9650, 30: 8930, 31: 9272, 32: 8705, 33: 9675, 34: 8867, 35: 9198, 36: 9065, 37: 8965, 38: 10446, 39: 9317, 40: 9832, 41: 8388, 42: 9425, 43: 8254, 44: 8390, 45: 8369, 46: 9538, 47: 9060, 48: 8208, 49: 8187, 50: 8541, 51: 8363, 52: 8240, 53: 9897, 54: 8743, 55: 8772, 56: 8720, 57: 8757, 58: 8444, 59: 8441, 60: 8814, 61: 8544, 62: 8288, 63: 9624, 64: 8403, 65: 8512, 66: 8110, 67: 9893, 68: 8173, 69: 10177, 70: 8678, 71: 8994, 72: 8746, 73: 10673, 74: 8819, 75: 8369, 76: 8909},
'unemployment_rate_1995': {0: 0.28999999165534973, 1: 1.6699999570846558, 2: 1.9500000476837158, 3: 4.639999866485596, 4: 3.8499999046325684, 5: 2.950000047683716, 6: 2.259999990463257, 7: 1.25, 8: 3.390000104904175, 9: 0.5600000023841858, 10: 0.44999998807907104, 11: 3.8299999237060547, 12: 2.7699999809265137, 13: 1.4199999570846558, 14: 3.130000114440918, 15: 1.1200000047683716, 16: 2.380000114440918, 17: 2.8299999237060547, 18: 3.130000114440918, 19: 2.6500000953674316, 20: 1.5099999904632568, 21: 1.100000023841858, 22: 1.7899999618530273, 23: 1.3899999856948853, 24: 2.4700000286102295, 25: 2.640000104904175, 26: 0.6499999761581421, 27: 1.6200000047683716, 28: 2.819999933242798, 29: 3.380000114440918, 30: 3.5199999809265137, 31: 2.799999952316284, 32: 5.75, 33: 6.429999828338623, 34: 1.0199999809265137, 35: 3.3299999237060547, 36: 4.460000038146973, 37: 7.079999923706055, 38: 7.340000152587891, 39: 6.489999771118164, 40: 3.319999933242798, 41: 2.4100000858306885, 42: 1.7200000286102295, 43: 2.7899999618530273, 44: 2.2799999713897705, 45: 1.7899999618530273, 46: 1.5099999904632568, 47: 1.7799999713897705, 48: 1.8899999856948853, 49: 4.829999923706055, 50: 2.509999990463257, 51: 2.5199999809265137, 52: 2.5299999713897705, 53: 1.600000023841858, 54: 1.8799999952316284, 55: 4.690000057220459, 56: 3.7300000190734863, 57: 3.380000114440918, 58: 3.240000009536743, 59: 3.450000047683716, 60: 4.760000228881836, 61: 1.2899999618530273, 62: 3.7899999618530273, 63: 1.600000023841858, 64: 5.739999771118164, 65: 3.509999990463257, 66: 5.769999980926514, 67: 4.090000152587891, 68: 0.44999998807907104, 69: 6.630000114440918, 70: 5.929999828338623, 71: 3.799999952316284, 72: 3.3299999237060547, 73: 4.75, 74: 5.380000114440918, 75: 4.730000019073486, 76: 4.010000228881836},
'unemployment_rate_1996': {0: 0.4300000071525574, 1: 1.850000023841858, 2: 2.2100000381469727, 3: 5.050000190734863, 4: 4.429999828338623, 5: 4.019999980926514, 6: 2.869999885559082, 7: 1.440000057220459, 8: 3.9700000286102295, 9: 0.5400000214576721, 10: 0.5899999737739563, 11: 4.309999942779541, 12: 3.259999990463257, 13: 1.7100000381469727, 14: 3.5999999046325684, 15: 1.5399999618530273, 16: 2.619999885559082, 17: 3.3499999046325684, 18: 3.9800000190734863, 19: 3.640000104904175, 20: 2.069999933242798, 21: 1.25, 22: 2.6600000858306885, 23: 2.009999990463257, 24: 2.680000066757202, 25: 3.0899999141693115, 26: 1.2899999618530273, 27: 2.009999990463257, 28: 3.5999999046325684, 29: 3.6700000762939453, 30: 4.199999809265137, 31: 3.2200000286102295, 32: 7.610000133514404, 33: 7.679999828338623, 34: 1.2100000381469727, 35: 4.28000020980835, 36: 5.389999866485596, 37: 8.229999542236328, 38: 9.399999618530273, 39: 7.070000171661377, 40: 4.480000019073486, 41: 2.940000057220459, 42: 2.5, 43: 3.759999990463257, 44: 2.890000104904175, 45: 2.309999942779541, 46: 1.809999942779541, 47: 2.440000057220459, 48: 2.259999990463257, 49: 5.449999809265137, 50: 2.9700000286102295, 51: 3.490000009536743, 52: 3.559999942779541, 53: 1.9600000381469727, 54: 2.430000066757202, 55: 4.980000019073486, 56: 4.5, 57: 3.950000047683716, 58: 3.4700000286102295, 59: 4.480000019073486, 60: 5.739999771118164, 61: 1.8600000143051147, 62: 4.519999980926514, 63: 2.309999942779541, 64: 5.71999979019165, 65: 4.119999885559082, 66: 6.550000190734863, 67: 4.71999979019165, 68: 7.010000228881836, 69: 7.75, 70: 5.570000171661377, 71: 4.789999961853027, 72: 3.740000009536743, 73: 5.440000057220459, 74: 5.659999847412109, 75: 5.880000114440918, 76: 5.559999942779541}

}

# District lookup
district_lookup = pd.DataFrame(district_data)

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
