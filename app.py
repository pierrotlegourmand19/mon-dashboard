import streamlit as st
import pandas as pd

st.title("LeanCure Dashboard")

fichier = st.file_uploader(
    "Importer un fichier Excel",
    type=["xlsx"]
)

if fichier:
    df = pd.read_excel(fichier)

    st.success("Fichier chargé")
    st.dataframe(df.head())
