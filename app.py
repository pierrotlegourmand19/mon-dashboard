import streamlit as st

st.title("Mon premier site Streamlit")

nom = st.text_input("Votre prénom")

if nom:
    st.success(f"Bonjour {nom} !")
