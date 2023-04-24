import pandas as pd
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pyttsx3
import speech_recognition as sr
import datetime
import base64
import wikipedia
import wikipediaapi
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 196)
engine.setProperty('volume', 2.7)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour >= 12 and hour <= 17:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("Hi sir!,I am jarvis sir.how can i help you")

with st.sidebar:
    selected = option_menu('Machine Learning in Finance',

                           ['Introduction',
                            'Income Prediction Using Census data',
                            'Bank Loan Repayment Prediction',
                            'Financial Queries'],
                           icons=['laptop','activity', 'heart', 'person'],
                           default_index=0)


if (selected == 'Introduction'):
    wish()
    st.title("Machine Learning in Finance ")
    st.text("Our Team:\n\n")
    st.text("\n1.Anand Kumar M   Assistant Professor  m_anandkumar@nitk.edu.in")
    st.text("\n2.M Hemanth Kumar     211AI025   mogilipalemhemanthkumar.211ai025@nitk.edu.in")
    st.text("\n3.J Deva Paul         211AI021   devapauljatti.211ai021@nitk.edu.in")
    st.text("\n4.Shashank Reddy M    211AI033   shashankreddymuppidi.211ai033@nitk.edu.in")
    st.text("\n5.Chudi Dhruv         211AI014   chudidhruv.211ai014@nitk.edu.in")
    speak("Welcome to the Machine Learning in finance ")
    speak("Our Team is")
    speak("Anand Kumar")
    speak("Mogilipalem Hemanth Kumar")
    speak("Jatti Deva Paul")
    speak("Shashank Reddy Muppidi")
    speak("Chudi Dhruv")
    speak("This Project Consists of Three different options")
    speak("Income Prediction Using census Data")
    speak("Bank Loan Re-Payment Prediction")
    speak("Financial Queries")
    speak("Have a Good Experience of our model")

if (selected == 'Income Prediction Using Census data'):

    add_bg_from_local('1.jfif')
    st.title("Income Prediction Using Census Data")
    df = pd.read_csv('adult.data')
    col1, col2, col3,col4 = st.columns(4)

    filename = 'Income.sav'
    data = pickle.load(open(filename, 'rb'))

    with col1:
     Age = st.number_input("Enter Your Age")
    with col2:
     work_class = st.selectbox("Select Your Work Class", (' State-gov', ' Self-emp-not-inc', ' Private', ' Federal-gov',
                                                         ' Local-gov', ' other', ' Self-emp-inc', ' Without-pay',
                                                         ' Never-worked'))
    with col3:
     Education = st.selectbox("Select Your Education ", (' Bachelors', ' HS-grad', ' 11th', ' Masters', ' 9th',
                                                        ' Some-college', ' Assoc-acdm', ' Assoc-voc', ' 7th-8th',
                                                        ' Doctorate', ' Prof-school', ' 5th-6th', ' 10th', ' 1st-4th',
                                                        ' Preschool', ' 12th'))
    with col1:
      Maritial_status = st.selectbox("Select Your Maritial Status ",
                                   (' Never-married', ' Married-civ-spouse', ' Divorced',
                                    ' Married-spouse-absent', ' Separated', ' Married-AF-spouse',
                                    ' Widowed'))
    with col2:
     Occupation = st.selectbox("Select Your Occupation", (' Adm-clerical', ' Exec-managerial', ' Handlers-cleaners',
                                                         ' Prof-specialty', ' Other-service', ' Sales', ' Craft-repair',
                                                         ' Transport-moving', ' Farming-fishing', ' Machine-op-inspct',
                                                         ' Tech-support', ' ?', ' Protective-serv', ' Armed-Forces',
                                                         ' Priv-house-serv'))
    with col3:
     Relationship = st.selectbox("Select Your RelationShip",
                                (' Not-in-family', ' Husband', ' Wife', ' Own-child', ' Unmarried',
                                 ' Other-relative'))
    with col1:
     Race = st.selectbox("select Your Race", (' White', ' Black', ' Asian-Pac-Islander', ' Amer-Indian-Eskimo',
                                             ' Other'))
    with col2:
     Sex = st.selectbox("Select Your Gender", (' Male', ' Female'))
    with col3:
     Capital_gain = st.number_input("Capital_gain")
    with col1:
     Caputal_loss = st.number_input("Caputal_loss")
    with col2:
     Hours_per_week = st.number_input("Hours_per_week")
    with col3:
     Native_country = st.selectbox("Select Native_country",
                                  (' Cuba', ' United-States', ' Jamaica', ' India', ' other', ' Mexico',
                                   ' South', ' Puerto-Rico', ' Honduras', ' England', ' Canada',
                                   ' Germany', ' Iran', ' Philippines', ' Italy', ' Poland',
                                   ' Columbia', ' Cambodia', ' Thailand', ' Ecuador', ' Laos',
                                   ' Taiwan', ' Haiti', ' Portugal', ' Dominican-Republic',
                                   ' El-Salvador', ' France', ' Guatemala', ' China', ' Japan',
                                   ' Yugoslavia', ' Peru', ' Outlying-US(Guam-USVI-etc)', ' Scotland',
                                   ' Trinadad&Tobago', ' Greece', ' Nicaragua', ' Vietnam', ' Hong',
                                   ' Ireland', ' Hungary', ' Holand-Netherlands'))


    def prediction(input_data):
        Prediction = data.predict(input_data)
        if (Prediction == 0):
            return "Your Income is Less than or Equal 50k"
        if (Prediction == 1):
            return "Your Income is Greater than 50k"


    if (st.button("Predict Income")):
        input_data = [Age, work_class, 122245, Education, 9, Maritial_status, Occupation, Relationship, Race, Sex,
                      Capital_gain, Caputal_loss, Hours_per_week, Native_country]
        x = pd.DataFrame([input_data], columns=['Age', 'work_class', 'Fnlwgt', 'Education', 'Education_num',
                                                'Maritial_status', 'Occupation', 'Relationship', 'Race', 'Sex',
                                                'Capital_gain', 'Caputal_loss', 'Hours_per_week', 'Native_country',
                                                ])
        x = x.replace([' State-gov', ' Self-emp-not-inc', ' Private', ' Federal-gov',
                       ' Local-gov', ' other', ' Self-emp-inc', ' Without-pay',
                       ' Never-worked'], [7, 6, 4, 1, 2, 0, 5, 8, 3])
        x = x.replace([' Bachelors', ' HS-grad', ' 11th', ' Masters', ' 9th',
                       ' Some-college', ' Assoc-acdm', ' Assoc-voc', ' 7th-8th',
                       ' Doctorate', ' Prof-school', ' 5th-6th', ' 10th', ' 1st-4th',
                       ' Preschool', ' 12th'], [9, 11, 1, 12, 6, 15, 7, 8, 5, 10, 14, 4, 0, 3, 13, 2])
        x = x.replace([' Never-married', ' Married-civ-spouse', ' Divorced',
                       ' Married-spouse-absent', ' Separated', ' Married-AF-spouse',
                       ' Widowed'], [4, 2, 0, 3, 5, 1, 6])
        x = x.replace([' Adm-clerical', ' Exec-managerial', ' Handlers-cleaners',
                       ' Prof-specialty', ' Other-service', ' Sales', ' Craft-repair',
                       ' Transport-moving', ' Farming-fishing', ' Machine-op-inspct',
                       ' Tech-support', ' other', ' Protective-serv', ' Armed-Forces',
                       ' Priv-house-serv'], [1, 4, 6, 10, 8, 12, 3, 14, 5, 7, 13, 0, 11, 2, 9])
        x = x.replace([' Not-in-family', ' Husband', ' Wife', ' Own-child', ' Unmarried',
                       ' Other-relative'], [1, 0, 5, 3, 4, 2])
        x = x.replace([' Cuba', 'United-States', ' Jamaica', ' India', ' ?', ' Mexico',
                       ' South', ' Puerto-Rico', ' Honduras', ' England', ' Canada',
                       ' Germany', ' Iran', ' Philippines', ' Italy', ' Poland',
                       ' Columbia', ' Cambodia', ' Thailand', ' Ecuador', ' Laos',
                       ' Taiwan', ' Haiti', ' Portugal', ' Dominican-Republic',
                       ' El-Salvador', ' France', ' Guatemala', ' China', ' Japan',
                       ' Yugoslavia', ' Peru', ' Outlying-US(Guam-USVI-etc)', ' Scotland',
                       ' Trinadad&Tobago', ' Greece', ' Nicaragua', ' Vietnam', ' Hong',
                       ' Ireland', ' Hungary', ' Holand-Netherlands'],
                      [5, 39, 23, 19, 0, 26, 35, 33, 16, 9, 2, 11, 20, 30, 22, 31, 4,
                       1, 37, 7, 25, 36, 14, 32, 6, 8, 10, 13, 3, 24, 41, 29, 28, 34,
                       38, 12, 27, 40, 17, 21, 18, 15])
        x = x.replace([' White', ' Black', ' Asian-Pac-Islander', ' Amer-Indian-Eskimo',
                       ' Other'], [4, 2, 1, 0, 3])
        x = x.replace([' Male', ' Female'], [1, 0])

        final_Prediction = prediction(x)
        st.success(final_Prediction)
        #speak(f"{final_Prediction}")


if (selected == 'Bank Loan Repayment Prediction'):
    add_bg_from_local('2.jfif')
    st.title("Bank Loan re-Payment Prediction")
    col1, col2, col3, col4 = st.columns(4)
    filename = "Bank1.sav"
    classifier = pickle.load(open(filename, 'rb'))


    def Prediction(input_data):
        x = classifier.predict(input_data)
        if (x == 1):
            return True
        else:
            return False


    with col1:
     Current_Loan_Amount = st.number_input("Current Loan Amount")
    with col2:
     Term = st.selectbox("Select Loan Term", ("Short term", "Long term"))
    with col3:
     Credit_Score = st.number_input("Credit Score")
    with col1:
     Annual_Income = st.number_input("Annual Income")
    with col2:
     Years_in_current_job = st.selectbox("Select Years in current job", (
    '8 years', '< 1 year', '2 years', '3 years', '10+ years', '4 years', '6 years', '7 years', '5 years', '1 year',
    '9 years'))
    with col3:
     Home_Ownership = st.selectbox("Select Home Ownership", ('Own Home', 'Home Mortgage', 'Rent', 'HaveMortgage'))
    with col1:
     Purpose = st.selectbox("Select Purpose", (
    'Debt Consolidation', 'Buy House', 'other', 'Take a Trip', 'Home Improvements', 'Other', 'Buy a Car',
    'Medical Bills', 'wedding', 'Business Loan', 'small_business', 'major_purchase', 'vacation', 'Educational Expenses',
    'moving', 'renewable_energy'))
    with col2:
     Monthly_Debt = st.number_input("Monthly Debt")
    with col3:
     Years_of_Credit_History = st.number_input("Years of Credit History")
    with col1:
     Months_since_last_delinquent = st.number_input("Months since last delinquent")
    with col2:
     Number_of_Open_Accounts = st.number_input("Number of Open Accounts")
    with col3:
     Number_of_Credit_Problems = st.number_input("Number of Credit Problems")
    with col1:
     Current_Credit_Balance = st.number_input("Current Credit Balance")
    with col2:
     Maximum_Open_Credit = st.number_input("Maximum Open Credit")
    with col3:
     Bankruptcies = st.number_input("Bankruptcies")
    with col1:
     Tax_Liens = st.number_input("Tax Liens")
    if st.button("Predict"):
        input_data = [Current_Loan_Amount, Term, Credit_Score, Annual_Income, Years_in_current_job, Home_Ownership,
                      Purpose,
                      Monthly_Debt, Years_of_Credit_History, Months_since_last_delinquent,
                      Number_of_Open_Accounts, Number_of_Credit_Problems, Current_Credit_Balance, Maximum_Open_Credit,
                      Bankruptcies, Tax_Liens]
        x = pd.DataFrame([input_data], columns=['Current Loan Amount', 'Term',
                                                'Credit Score', 'Annual Income', 'Years in current job',
                                                'Home Ownership', 'Purpose', 'Monthly Debt', 'Years of Credit History',
                                                'Months since last delinquent', 'Number of Open Accounts',
                                                'Number of Credit Problems', 'Current Credit Balance',
                                                'Maximum Open Credit', 'Bankruptcies', 'Tax Liens'])

        x = x.replace(['Own Home', 'Home Mortgage', 'Rent', 'HaveMortgage'], [2, 1, 3, 0])
        x = x.replace(["Short term", "Long term"], [1, 0])
        x = x.replace(['Debt Consolidation', 'Buy House', 'other', 'Take a Trip',
                       'Home Improvements', 'Other', 'Buy a Car', 'Medical Bills',
                       'wedding', 'Business Loan', 'small_business', 'major_purchase',
                       'vacation', 'Educational Expenses', 'moving', 'renewable_energy'],
                      [3, 1, 11, 8, 5, 7, 2, 6, 15, 0, 13, 9, 14, 4, 10, 12])
        x = x.replace(
            ['8 years', '< 1 year', '2 years', '3 years', '10+ years', '4 years', '6 years', '7 years', '5 years',
             '1 year', '9 years'], [8, 10, 2, 3, 1, 4, 6, 7, 5, 0, 9])

        predict = Prediction(x)
        if (predict):
            st.success("Person can re-Pay Loan")
            #speak("Person can re-Pay Loan")
        else:
            st.success("Person can't re-Pay Loan")
            #speak("Person can't re-Pay Loan")

if (selected == 'Financial Queries'):
   # speak("Welcome to Financial Queries")
    st.title("Financial Queries")

    query = st.text_input("Enter the Query: ", key='query1')
    wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )
    p_wiki = wiki.page(query)
    if st.button("Search"):
        if not p_wiki.exists():
            st.success("Right now this query can't be answered, Our team is working  on that")
            speak("Right now this query can't be answered, Our team is working  on that")
        else:
            st.success(p_wiki.text[0:500])




