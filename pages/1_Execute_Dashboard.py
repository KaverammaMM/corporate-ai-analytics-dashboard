import streamlit as st
from utils.data_loader import load_data
from utils.charts import adoption_trend
from utils.insights import generate_insights

df = load_data()

st.title("📈 Executive Dashboard")

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Companies",
    len(df)
)

col2.metric(
    "Avg Adoption",
    round(df["ai_adoption_level"].mean(),2)
)

col3.metric(
    "Avg Maturity",
    round(df["ai_maturity_score"].mean(),2)
)

col4.metric(
    "Deployments",
    int(df["deployment_count"].sum())
)

st.plotly_chart(
    adoption_trend(df),
    use_container_width=True
)

st.subheader("AI Insights")

for item in generate_insights(df):
    st.success(item)
