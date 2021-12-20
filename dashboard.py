import streamlit as st
import pandas as pd
import pickle
import numpy as np

# loading the trained model
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

st.title("Loan Approval Predictor")


@st.cache
def prediction(Gender, Married, ApplicantIncome, LoanAmount,
               Credit_History):

    if Gender == 'male':
        Gender = 1
    else:
        Gender = 0

    if Married == 'Unmarried':
        Married = 0
    else:
        Married = 1

    if Credit_History == 'Unclear Debts':
        Credit_History = 0
    else:
        Credit_History = 1

    LoanAmount = LoanAmount / 1000

    prediction = classifier.predict([[Gender, Married, ApplicantIncome, LoanAmount,
                                      Credit_History]])

    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred


def main():

    # display the front end aspect
    st.write()
    st.title('Loan Prediction App')
    st.markdown('loan Approval Prediction')


pred = 'Approved'

Gender = st.selectbox('Gender', ('Male', 'Female'))
Married = st.selectbox('Marital Status', ('Married', 'Unmarried'))
ApplicantIncome = st.number_input('Applicants Monthly Income')
LoanAmount = st.number_input('Total Loan Amount')
Credit_History = st.selectbox(
    'Credit History', ('Unclear Debts', 'No Unclear debts'))

result = ""

if st.button('Predict'):
    result = prediction(Gender, Married, ApplicantIncome,
                        LoanAmount, Credit_History)
st.success('Your loan is{}'.format(result))
print(LoanAmount)
