import streamlit as st
from utils.data_loader import load_data
from utils.charts import country_revenue

df = load_data()

st.title("🌎 Country Analytics")

st.plotly_chart(
    country_revenue(df),
    use_container_width=True
)
