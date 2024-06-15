import pickle
import streamlit as st

# membaca model 
anemia_model = pickle.load (open("anemia_model.sav", "rb" ))

# judul web 
st.title ("ANEMIA PREDICTION")

# membagi kolom 
col1, col2, col3, col4 = st.columns (4)

with col1 :
    Pregnancies = st.text_input ("Pregnancies")

with col2 :
    Glucose = st.text_input ("Glucose")

with col3 :
    BloodPressure = st.text_input ("Bloodpressure")

with col4 :
    SkinThickness = st.text_input ("SkinThickness")

with col1 :
    Insulin = st.text_input ("Insulin")

with col2 :
    BMI = st.text_input ("BMI")

with col3 :
    AnemiaPedigreeFunction = st.text_input ("Anemia Pedigree Function")

with col4 :
    Age = st.text_input ("Age")


# kode untuk meemprediksi 
anemia_diagnosis = ""

# membuat tombol untuk prediksi 
if st.button ("Predicting Anemia"):
    anemia_prediction = anemia_model.predict ([[Pregnancies, Glucose,  BloodPressure,  SkinThickness, Insulin, BMI, AnemiaPedigreeFunction, Age  ]])

    if (anemia_prediction[0] == 0):
        anemia_diagnosis = "normal"
    else :
        anemia_diagnosis = "anemia"
    st.success (anemia_diagnosis) 
