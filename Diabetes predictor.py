# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 19:44:11 2023

@author: ASUS
"""

import numpy as np
import pickle
import streamlit as st

# load saved model
loaded_model = pickle.load(open('D:/Tugas Kuliah s3/project_AI/using_random_forest/trained_model.sav', 'rb'))

#function for prediction
def diabetes_prediction(input_data):
    
    # mengubah input menjadi numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # mengubah bentuk array karena hanya prediksi satu
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if (prediction[0] == 0):
        return 'Tidak terindikasi diabetes. Tetap jaga pola makan dan berolahraga secukupnya'
    else:
        return 'Ada indikasi diabetes/pra-diabetes. Jaga pola makan dengan kurangi konsumsi gula dan berolahraga'
    
def main():
    
    # title
    st.title('Diagnosis Cepat Diabetes Rumah Sakit Sehat Bahagia')
    
    # kolom input
    pregnancies = st.number_input(label='Jumlah kehamilan', step=1.0, format='%.0f')
    glucose = st.number_input(label='Kadar glukosa (tes glukometer) (mg/dL)', step=1.0, format='%.0f')
    bloodpressure = st.number_input(label='Tekanan darah diastolic (mm/Hg)', step=1.0, format='%.0f')
    massa = st.number_input(label='Berat badan (kg)', step=1.0, format='%.0f')
    tinggi = st.number_input(label='Tinggi badan (cm)', step=1.0, format='%.0f')
    if tinggi!=0:
        bmi = str(massa/(tinggi/100)**2)
    age = st.number_input(label='Usia (tahun)', step=1.0, format='%.0f')
    
    diagnosis = ''
    
    # tombol proses
    if st.button('Cek hasil'):
        diagnosis = diabetes_prediction([pregnancies, glucose, bloodpressure, bmi, age])
    
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
        
    
    
    
    