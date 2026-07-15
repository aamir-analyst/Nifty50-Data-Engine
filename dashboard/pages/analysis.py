import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from config.config import PROCESSED_DIR, REPORT_DIR


def show():

    st.title("📊 Live Stock Analysis")

    feature_file = PROCESSED_DIR / "features.csv"
    prediction_file = REPORT_DIR / "market_predictions.csv"

    if not feature_file.exists():
        st.error("Run: python main.py --features")
        return

    if not prediction_file.exists():
        st.error("Run: python main.py --predict")
        return

    df = pd.read_csv(feature_file)
    pred = pd.read_csv(prediction_file)

    df["Date"] = pd.to_datetime(df["Date"])

    stock = st.selectbox(

        "Select Stock",

        sorted(df.Symbol.unique())

    )

    stock_df = (
        df[df.Symbol == stock]
        .sort_values("Date")
    )

    latest = pred[
        pred.Symbol == stock
    ].iloc[0]

    # ===========================
    # KPI
    # ===========================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Current",
        f"₹{latest['Current']:.2f}"
    )

    c2.metric(
        "Prediction",
        f"₹{latest['Prediction']:.2f}"
    )

    c3.metric(
        "Return",
        f"{latest['Expected Return %']:.2f}%"
    )

    c4.metric(
        "Signal",
        latest["Signal"]
    )

    st.divider()

    # ===========================
    # Candlestick
    # ===========================

    fig = go.Figure()

    fig.add_trace(

        go.Candlestick(

            x=stock_df.Date,

            open=stock_df.Open,

            high=stock_df.High,

            low=stock_df.Low,

            close=stock_df.Close,

            name="Price"

        )

    )

    fig.add_trace(

        go.Scatter(

            x=stock_df.Date,

            y=stock_df.EMA_20,

            name="EMA20"

        )

    )

    fig.add_trace(

        go.Scatter(

            x=stock_df.Date,

            y=stock_df.EMA_50,

            name="EMA50"

        )

    )

    fig.update_layout(

        height=700,

        xaxis_rangeslider_visible=False

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    # ===========================
    # RSI
    # ===========================

    rsi = go.Figure()

    rsi.add_trace(

        go.Scatter(

            x=stock_df.Date,

            y=stock_df.RSI_14,

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

    st.divider()

    # ===========================
    # AI Insight
    # ===========================

    st.subheader("🤖 AI Insight")

    signal = latest["Signal"]

    if signal == "STRONG BUY":

        st.success(
            "Model expects strong upside."
        )

    elif signal == "BUY":

        st.success(
            "Positive momentum detected."
        )

    elif signal == "HOLD":

        st.warning(
            "No strong edge currently."
        )

    elif signal == "SELL":

        st.error(
            "Weakness detected."
        )

    else:

        st.error(
            "Strong downside risk."
        )