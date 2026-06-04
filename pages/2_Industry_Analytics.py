import streamlit as st
from utils.data_loader import load_data
from utils.charts import industry_adoption

df = load_data()

st.title("🏭 Industry Analytics")

st.plotly_chart(
    industry_adoption(df),
    use_container_width=True
)
