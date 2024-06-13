import pickle
import streamlit as st

# membaca model 
anemia_model = pickle.load (open("anemia_model.sav", "rb" ))

# judul web 
st.title ("memprediksi anemia")

# membagi kolom 
col1, col2, col3, col4 = st.columns (4)

with col1 :
    Pregnancies = st.text_input ("input nilai pregnancies")

with col2 :
    Glucose = st.text_input ("input nilai glucose")

with col3 :
    BloodPressure = st.text_input ("input nilai Bloodpressure")

with col4 :
    SkinThickness = st.text_input ("input nilai SkinThickness")

with col1 :
    Insulin = st.text_input ("input nilai Insulin")

with col2 :
    BMI = st.text_input ("input nilai BMI")

with col3 :
    AnemiaPedigreeFunction = st.text_input (" input nilai AnemiaPedigreeFunction")

with col4 :
    Age = st.text_input ("inpu nilai Age")


# kode untuk meemprediksi 
anemia_diagnosis = ""

# membuat tombol untuk prediksi 
if st.button ("memprediksi anemia"):
    anemia_prediction = anemia_model.predict ([[Pregnancies, Glucose,  BloodPressure,  SkinThickness, Insulin, BMI, AnemiaPedigreeFunction, Age  ]])

    if (anemia_prediction[0] == 0):
        anemia_diagnosis = "normal"
    else :
        anemia_diagnosis = "anemia"
    st.success (anemia_diagnosis) 
