import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("loan_model.pkl", "rb"))

st.title("Loan Approval Prediction System")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])

applicant_income = st.number_input("Applicant Income", min_value=0)

loan_amount = st.number_input("Loan Amount", min_value=0)

credit_history = st.selectbox("Credit History", [1, 0])

if st.button("Predict"):

    # Simple encoding
    gender = 1 if gender == "Male" else 0
    married = 1 if married == "Yes" else 0

    input_data = pd.DataFrame([[gender,
                                married,
                                0,
                                0,
                                0,
                                applicant_income,
                                0,
                                loan_amount,
                                360,
                                credit_history,
                                2,
                                applicant_income]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Rejected ❌")