import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path="data/corporate_ai_adoption_dataset.csv"):
    """
    Loads large corporate AI dataset efficiently with caching
    """
    df = pd.read_csv(path)

    # Basic cleanup (safe defaults)
    df.columns = df.columns.str.lower().str.strip()

    return df
