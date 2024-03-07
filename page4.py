import streamlit as st

def page_4():
    st.title("Hitung luas persegi panjang")
panjang = st.number_input("Masukan nilai panjang",0)
lebar = st.number_input("Masukan nilai lebar",0)
hitung = st.button("hitung luas")
    
if hitung:
    luas = panjang * lebar
    st.write("luas persegi panjang adalah=",luas)
    
