import streamlit as st 
import pandas as pd
from page1 import page_1
from page2 import page_2
from page3 import page_3

# st.write("Coding club 2024 ")
# df = pd.DataFrame({
#     'No':[1,2,3,4],
#     'Nama' :['Harni','Zahwa','Nadia','Amanda'],
#     'Nilai':[94,100,96,95]

# })

# df


PAGES ={
    "page 1" : page_1,
    "page 2" : page_2,
    "page 3" : page_3
    }
st.sidebar.image("harni.jpeg",width=100)
page =  st.sidebar.radio("Halaman",list(PAGES.keys()))
PAGES[page]()

