import streamlit as st
import pickle
import pandas as pd
import numpy as np
st.title("Bank Loan re-Payment Prediction")
filename="Bank1.sav"
classifier=pickle.load(open(filename,'rb'))
def Prediction(input_data):
  x=classifier.predict(input_data)
  if(x==1):
    return True
  else:
    return False
Current_Loan_Amount	=st.number_input("Current Loan Amount")
Term=st.selectbox("Select Loan Term", ("Short term", "Long term"))
Credit_Score=st.number_input("Credit Score")
Annual_Income=st.number_input("Annual Income")
Years_in_current_job=st.selectbox("Select Years in current job", ('8 years', '< 1 year', '2 years', '3 years', '10+ years','4 years', '6 years', '7 years', '5 years', '1 year', '9 years'))
Home_Ownership=st.selectbox("Select Home Ownership", ('Own Home', 'Home Mortgage', 'Rent', 'HaveMortgage'))
Purpose=st.selectbox("Select Purpose", ('Debt Consolidation', 'Buy House', 'other', 'Take a Trip', 'Home Improvements', 'Other', 'Buy a Car', 'Medical Bills', 'wedding', 'Business Loan', 'small_business', 'major_purchase','vacation', 'Educational Expenses', 'moving', 'renewable_energy'))
Monthly_Debt=st.number_input("Monthly Debt")
Years_of_Credit_History=st.number_input("Years of Credit History")
Months_since_last_delinquent=st.number_input("Months since last delinquent")
Number_of_Open_Accounts=st.number_input("Number of Open Accounts")
Number_of_Credit_Problems=st.number_input("Number of Credit Problems")
Current_Credit_Balance=st.number_input("Current Credit Balance")
Maximum_Open_Credit=st.number_input("Maximum Open Credit")
Bankruptcies=st.number_input("Bankruptcies")
Tax_Liens=st.number_input("Tax Liens")
if st.button("Predict"):
    input_data = [Current_Loan_Amount, Term, Credit_Score, Annual_Income, Years_in_current_job, Home_Ownership, Purpose,
                  Monthly_Debt, Years_of_Credit_History, Months_since_last_delinquent,
                  Number_of_Open_Accounts, Number_of_Credit_Problems, Current_Credit_Balance, Maximum_Open_Credit,
                  Bankruptcies, Tax_Liens]
    x=pd.DataFrame([input_data],columns=['Current Loan Amount', 'Term',
       'Credit Score', 'Annual Income', 'Years in current job',
       'Home Ownership', 'Purpose', 'Monthly Debt', 'Years of Credit History',
       'Months since last delinquent', 'Number of Open Accounts',
       'Number of Credit Problems', 'Current Credit Balance',
       'Maximum Open Credit', 'Bankruptcies', 'Tax Liens'])

    x=x.replace(['Own Home', 'Home Mortgage', 'Rent', 'HaveMortgage'],[2,1,3,0])
    x= x.replace(["Short term", "Long term"], [1, 0])
    x=x.replace(['Debt Consolidation', 'Buy House', 'other', 'Take a Trip',
       'Home Improvements', 'Other', 'Buy a Car', 'Medical Bills',
       'wedding', 'Business Loan', 'small_business', 'major_purchase',
       'vacation', 'Educational Expenses', 'moving', 'renewable_energy'],[ 3,  1, 11,  8,  5,  7,  2,  6, 15,  0, 13,  9, 14,  4, 10, 12])
    x=x.replace(['8 years', '< 1 year', '2 years', '3 years', '10+ years','4 years', '6 years', '7 years', '5 years', '1 year', '9 years'],[ 8, 10,  2,  3,  1,  4,  6,  7,  5,  0,  9])

    predict=Prediction(x)
    if(predict):
        st.success("Person can re-Pay Loan")
    else:
        st.success("Person can't re-Pay Loan")

