import plotly.express as px
import plotly.graph_objects as go

# =========================
# AI Adoption Trend
# =========================
def ai_adoption_trend(df):
    trend = df.groupby("year")["ai_adoption_level"].mean().reset_index()

    fig = px.line(
        trend,
        x="year",
        y="ai_adoption_level",
        markers=True,
        title="📈 AI Adoption Trend Over Time"
    )
    return fig


# =========================
# Industry Adoption
# =========================
def industry_adoption_chart(df):
    data = df.groupby("industry")["ai_adoption_level"].mean().reset_index()

    fig = px.bar(
        data.sort_values("ai_adoption_level", ascending=False),
        x="industry",
        y="ai_adoption_level",
        color="ai_adoption_level",
        title="🏭 AI Adoption by Industry"
    )
    return fig


# =========================
# Revenue Impact
# =========================
def revenue_by_country(df):
    data = df.groupby("country")["revenue_impact"].sum().reset_index()

    fig = px.choropleth(
        data,
        locations="country",
        locationmode="country names",
        color="revenue_impact",
        title="🌍 Revenue Impact by Country"
    )
    return fig


# =========================
# Correlation Heatmap
# =========================
def correlation_heatmap(df):
    corr = df.select_dtypes(include=["number"]).corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        title="🔗 Feature Correlation Heatmap",
        color_continuous_scale="Viridis"
    )
    return fig
