import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    """
    Load and cache the dataset
    """
    df = pd.read_csv('D:\\Kuliah\\SEM 6\\BahasaAlami\\Modul 2\\modul2_Classification_Text\\data\\train_preprocess.csv')
    return df
