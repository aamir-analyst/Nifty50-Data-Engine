import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from config.config import PROCESSED_DIR


def show():

    st.title("📉 Historical Stock Charts")

    st.caption("Interactive Price Analysis")

    st.markdown("---")

    data_file = PROCESSED_DIR / "features.csv"

    if not data_file.exists():

        st.error("Feature dataset not found.")

        st.info("Run: python main.py --features")

        return

    df = pd.read_csv(data_file)

    df["Date"] = pd.to_datetime(df["Date"])

    # ======================================
    # STOCK SELECTION
    # ======================================

    stock = st.selectbox(

        "Select Stock",

        sorted(df["Symbol"].unique())

    )

    stock_df = (
        df[df["Symbol"] == stock]
        .sort_values("Date")
        .copy()
    )

    # ======================================
    # DATE FILTER
    # ======================================

    start_date = st.date_input(
        "Start Date",
        stock_df["Date"].min().date()
    )

    end_date = st.date_input(
        "End Date",
        stock_df["Date"].max().date()
    )

    stock_df = stock_df[
        (stock_df["Date"] >= pd.Timestamp(start_date)) &
        (stock_df["Date"] <= pd.Timestamp(end_date))
    ]

    # ======================================
    # CANDLESTICK
    # ======================================

    fig = go.Figure()

    fig.add_trace(

        go.Candlestick(

            x=stock_df["Date"],

            open=stock_df["Open"],

            high=stock_df["High"],

            low=stock_df["Low"],

            close=stock_df["Close"],

            name="Price"

        )

    )

    fig.add_trace(

        go.Scatter(

            x=stock_df["Date"],

            y=stock_df["EMA_20"],

            name="EMA 20"

        )

    )

    fig.add_trace(

        go.Scatter(

            x=stock_df["Date"],

            y=stock_df["EMA_50"],

            name="EMA 50"

        )

    )

    fig.update_layout(

        title=f"{stock} Price Chart",

        height=700,

        xaxis_rangeslider_visible=False

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ======================================
    # VOLUME
    # ======================================

    st.subheader("📊 Trading Volume")

    volume = go.Figure()

    volume.add_trace(

        go.Bar(

            x=stock_df["Date"],

            y=stock_df["Volume"]

        )

    )

    volume.update_layout(

        height=300

    )

    st.plotly_chart(

        volume,

        use_container_width=True

    )

    # ======================================
    # RSI
    # ======================================

    st.subheader("📈 RSI Indicator")

    rsi = go.Figure()

    rsi.add_trace(

        go.Scatter(

            x=stock_df["Date"],

            y=stock_df["RSI_14"],

            name="RSI"

        )

    )

    rsi.add_hline(y=70)

    rsi.add_hline(y=30)

    rsi.update_layout(height=300)

    st.plotly_chart(

        rsi,

        use_container_width=True

    )