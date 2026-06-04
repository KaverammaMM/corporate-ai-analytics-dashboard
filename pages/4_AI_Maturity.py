import streamlit as st
from utils.data_loader import load_data
from utils.charts import maturity_distribution

df = load_data()

st.title("🎯 AI Maturity Analytics")

st.plotly_chart(
    maturity_distribution(df),
    use_container_width=True
)
