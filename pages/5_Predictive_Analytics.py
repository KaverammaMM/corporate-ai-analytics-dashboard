import streamlit as st
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

from utils.data_loader import load_data

df = load_data()

st.title("🔮 Predictive Analytics")

features = [
    "ai_adoption_level",
    "automation_rate",
    "employee_ai_training_hours",
    "deployment_count"
]

X = df[features]
y = df["revenue_impact"]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train,y_train)

st.success("Revenue Prediction Model Trained")

importance = pd.DataFrame({
    "Feature":features,
    "Importance":model.feature_importances_
})

st.dataframe(
    importance.sort_values(
        "Importance",
        ascending=False
    )
)
