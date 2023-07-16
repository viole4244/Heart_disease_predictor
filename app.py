import streamlit as st
import numpy as np
import pandas as pd
import pickle
pickle_in=open("Classifier.pkl","rb")
model=pickle.load(pickle_in)

def welcome():
    return "Welcome All"


def heart_disease(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    prediction=model.predict([[float(age),float(sex),float(cp),float(trestbps),float(chol),float(fbs),float(restecg),float(thalach),float(exang),float(oldpeak),float(slope),float(ca),float(thal)]])
    print(prediction)
    return prediction

def main():
    st.title("Heart Disease Perdictor")
    html_temp = """
    <div style="background-color:pink;padding:10px">
    <h2 style="color:blue;text-align:center;">Streamlit Heart Disease Predictor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("Age","Type Here")
    Sex = st.selectbox("sex",[0,1])
    cp = st.selectbox("Chest Pain Type",[0,1,2])
    trestbps = st.text_input("Resting blood pressure","Type Here")
    chol=st.text_input("Cholestrol level","Type Here")
    fbs=st.selectbox("Fasting blood sugar",[0,1])
    restecg=st.selectbox("Resting electrocardiographic result",[0,1])
    thalach=st.text_input("Maximum heart rate","Type Here")
    exang=st.selectbox("Exercise induced angina",[0,1])
    oldpeak=st.text_input("exercise relative to rest","Type Here")
    slope=st.selectbox("slope of the peak exercise ST segment",[0,1,2])
    ca=st.text_input("The number of major vessels","Type Here")
    thal=st.text_input("thalassemia","Type Here")
    result=""
    if st.button("Predict"):
        result=heart_disease(age,Sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    if result==1:
       st.success('The Person has heart disease')
    elif result==0:
        st.success('The Person does not have a heart disease') 
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")
if __name__=='__main__':
    main()
