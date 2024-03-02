import streamlit as st 
import pandas as pd


# st.write("Coding club 2024 ")
# df = pd.DataFrame({
#     'No':[1,2,3,4],
#     'Nama' :['Harni','Zahwa','Nadia','Amanda'],
#     'Nilai':[94,100,96,95]

# })

# df

def page_1():
    st.title("Halaman 1")
    st.write('Halaman ini digunakan untuk Intro')
def page_2():
    st.title("Halaman 2")
    st.write('Halaman ini digunakan untuk  Menampilkan Youtube video')
def page_3():
    st.title("Halaman 3")
    st.write('Halaman ini digunakan untuk Menampilkan Rumus Matematika')

PAGES ={
    "page 1" : page_1,
    "page 2" : page_2,
    "page 3" : page_3
    }

page =  st.sidebar.radio("Halaman",list(PAGES.keys()))
PAGES[page]()

