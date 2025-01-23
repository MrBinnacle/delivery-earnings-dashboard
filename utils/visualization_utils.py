import plotly.express as px

def plot_earnings_over_time(df):
    """Plot earnings trends over time."""
    fig = px.line(
        df,
        x="order_date",
        y="total_earnings",
        title="Earnings Over Time",
        markers=True,
        labels={"total_earnings": "Total Earnings", "order_date": "Date"},
    )
    return fig

def plot_earnings_contributions(df):
    """Plot contributions of base_pay, tips, peak_pay, and adjustments."""
    df_grouped = df.groupby("order_date")[["base_pay", "tips", "peak_pay", "adjustments"]].sum().reset_index()
    fig = px.bar(
        df_grouped,
        x="order_date",
        y=["base_pay", "tips", "peak_pay", "adjustments"],
        title="Earnings Contribution by Date",
        labels={"value": "Earnings", "variable": "Contribution Type"},
        barmode="stack",
    )
    return fig
