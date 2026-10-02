import streamlit as st
import pandas as pd
import os


# ============================================================
# CRYPTOCURRENCY PRICE TRACKER - DASHBOARD
# ============================================================

st.set_page_config(
    page_title="Cryptocurrency Price Tracker",
    page_icon="₿",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("₿ Cryptocurrency Price Tracker")
st.caption("Real-Time Cryptocurrency Market Monitoring Dashboard")


# ============================================================
# LOAD CSV DATA
# ============================================================

CSV_FILE = "crypto_data.csv"


if not os.path.exists(CSV_FILE):

    st.error(
        "crypto_data.csv not found. "
        "Please run the tracker first."
    )

    st.stop()


df = pd.read_csv(CSV_FILE)


# ============================================================
# DATA VALIDATION
# ============================================================

required_columns = [
    "timestamp",
    "name",
    "symbol",
    "price_usd",
    "change_24h_pct",
    "market_cap_usd"
]


missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]


if missing_columns:

    st.error(
        f"Missing columns: {missing_columns}"
    )

    st.stop()


# ============================================================
# DATA CLEANING
# ============================================================

df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    errors="coerce"
)

df["price_usd"] = pd.to_numeric(
    df["price_usd"],
    errors="coerce"
)

df["change_24h_pct"] = pd.to_numeric(
    df["change_24h_pct"],
    errors="coerce"
)

df["market_cap_usd"] = pd.to_numeric(
    df["market_cap_usd"],
    errors="coerce"
)


df = df.dropna(
    subset=[
        "timestamp",
        "name",
        "price_usd",
        "change_24h_pct"
    ]
)


# ============================================================
# LATEST DATA
# ============================================================

latest_timestamp = df["timestamp"].max()

latest_data = df[
    df["timestamp"] == latest_timestamp
].copy()


# ============================================================
# SUMMARY METRICS
# ============================================================

total_coins = len(latest_data)

total_records = len(df)

average_change = latest_data[
    "change_24h_pct"
].mean()

highest_price = latest_data[
    "price_usd"
].max()


# ============================================================
# DASHBOARD METRICS
# ============================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Coins Tracked",
        total_coins
    )


with col2:

    st.metric(
        "Total Records",
        total_records
    )


with col3:

    st.metric(
        "Average 24h Change",
        f"{average_change:.2f}%"
    )


with col4:

    st.metric(
        "Highest Price",
        f"${highest_price:,.2f}"
    )


st.divider()


# ============================================================
# LATEST MARKET DATA
# ============================================================

st.subheader("📊 Latest Cryptocurrency Data")


display_columns = [
    "name",
    "symbol",
    "price_usd",
    "change_24h_pct",
    "market_cap_usd"
]


display_df = latest_data[
    display_columns
].copy()


display_df.columns = [
    "Name",
    "Symbol",
    "Price (USD)",
    "24h Change (%)",
    "Market Cap (USD)"
]


st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# TOP GAINERS
# ============================================================

st.subheader("🚀 Top Gainers")


top_gainers = latest_data.sort_values(
    by="change_24h_pct",
    ascending=False
).head(5)


for _, row in top_gainers.iterrows():

    st.write(
        f"**{row['name']} ({row['symbol']})** "
        f"→ {row['change_24h_pct']:.2f}%"
    )


# ============================================================
# TOP LOSERS
# ============================================================

st.subheader("📉 Top Losers")


top_losers = latest_data.sort_values(
    by="change_24h_pct",
    ascending=True
).head(5)


for _, row in top_losers.iterrows():

    st.write(
        f"**{row['name']} ({row['symbol']})** "
        f"→ {row['change_24h_pct']:.2f}%"
    )


# ============================================================
# PRICE COMPARISON
# ============================================================

st.subheader("💰 Cryptocurrency Price Comparison")


price_chart = latest_data[
    ["name", "price_usd"]
].set_index("name")


st.bar_chart(
    price_chart
)


# ============================================================
# 24H CHANGE CHART
# ============================================================

st.subheader("📈 24-Hour Price Change")


change_chart = latest_data[
    ["name", "change_24h_pct"]
].set_index("name")


st.bar_chart(
    change_chart
)


# ============================================================
# HISTORICAL PRICE DATA
# ============================================================

st.subheader("📈 Historical Price Tracking")


selected_coin = st.selectbox(
    "Select Cryptocurrency",
    sorted(df["name"].unique())
)


coin_history = df[
    df["name"] == selected_coin
].sort_values("timestamp")


coin_history = coin_history[
    ["timestamp", "price_usd"]
].set_index("timestamp")


st.line_chart(
    coin_history
)


# ============================================================
# LAST UPDATED
# ============================================================

st.divider()

st.info(
    f"Last updated: {latest_timestamp}"
)


# ============================================================
# FOOTER
# ============================================================

st.caption(
    "Data source: CoinMarketCap | "
    "Powered by Python, Selenium, Pandas and Streamlit"
)