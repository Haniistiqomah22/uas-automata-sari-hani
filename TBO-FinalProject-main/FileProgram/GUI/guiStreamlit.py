from Algorithm.checking import cek_kalimat

import sys
sys.path.append(r"C:\Users\Lutviana\AppData\Local\Programs\Python\Python310\Lib\site-packages\streamlit")
import streamlit as st

def runStreamlit():
    st.write("""
    # Aplikasi Cek Bahasa Indonesia
    Simple Application for Checking *Standard Sentence Pattern* for Fulfill The Final Project of the "Teori Bahasa dan Automata".
    _____________________________________
   Anggota Kelompok :
   Hani Istiqomah (210111003)
   Sari Andini Putri (210111005)
    """)

    input = st.text_input("Input the String that you want to check:")
    cek = st.button("Check It!")

    if cek:
        if cek_kalimat(input) == 1:
            st.success("It's Standard Sentence! Congratulations...")
        else:
            st.error("Unfortunately, Your String is non-Standard. Try Again!")