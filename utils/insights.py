def generate_insights(df):
    """
    Generates business insights from AI dataset
    """

    insights = []

    avg_adoption = df["ai_adoption_level"].mean()
    avg_maturity = df["ai_maturity_score"].mean()
    total_revenue = df["revenue_impact"].sum()

    top_industry = (
        df.groupby("industry")["ai_adoption_level"]
        .mean()
        .idxmax()
    )

    top_country = (
        df.groupby("country")["revenue_impact"]
        .sum()
        .idxmax()
    )

    insights.append(f"📊 Average AI Adoption Level: {avg_adoption:.2f}")
    insights.append(f"🎯 Average AI Maturity Score: {avg_maturity:.2f}")
    insights.append(f"💰 Total Revenue Impact: ${total_revenue:,.0f}")
    insights.append(f"🏭 Top AI-Adopting Industry: {top_industry}")
    insights.append(f"🌍 Highest Revenue Country: {top_country}")

    # Advanced insight
    if avg_adoption > 70:
        insights.append("🚀 Organization is in HIGH AI maturity stage")
    else:
        insights.append("⚠️ Organization is in EARLY AI adoption stage")

    return insights
