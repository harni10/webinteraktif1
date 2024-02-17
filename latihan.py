import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("Coding club 2024 ")
df = pd.DataFrame({
    'No':[1,2,3,4],
    'Nama' :['Harni','Zahwa','Nadia','Amanda'],
    'Nilai':[94,100,96,95]

})

df