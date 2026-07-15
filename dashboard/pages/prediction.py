import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from config.config import REPORT_DIR


def show():

    st.title("🤖 AI Stock Prediction")

    st.caption("Random Forest Based Prediction Engine")

    st.markdown("---")

    prediction_file = REPORT_DIR / "market_predictions.csv"

    if not prediction_file.exists():

        st.error("Prediction report not found.")

        st.info("Run : python main.py --predict")

        return

    df = pd.read_csv(prediction_file)

    # ======================================================
    # STOCK SELECTION
    # ======================================================

    stock = st.selectbox(

        "Select Stock",

        sorted(df["Symbol"])

    )

    row = df[df["Symbol"] == stock].iloc[0]

    current = float(row["Current"])

    prediction = float(row["Prediction"])

    expected = float(row["Expected Return %"])

    signal = row["Signal"]

    # ======================================================
    # KPI CARDS
    # ======================================================

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "💰 Current Price",
        f"₹ {current:,.2f}"
    )

    c2.metric(
        "🎯 Predicted Price",
        f"₹ {prediction:,.2f}"
    )

    c3.metric(
        "📈 Expected Return",
        f"{expected:.2f}%"
    )

    st.markdown("---")

    # ======================================================
    # SIGNAL
    # ======================================================

    if "BUY" in signal:

        st.success(f"🟢 {signal}")

    elif "SELL" in signal:

        st.error(f"🔴 {signal}")

    else:

        st.warning(f"🟡 {signal}")

    # ======================================================
    # PRICE COMPARISON
    # ======================================================

    st.subheader("📊 Price Comparison")

    fig = go.Figure()

    fig.add_trace(

        go.Bar(

            x=["Current"],

            y=[current],

            name="Current"

        )

    )

    fig.add_trace(

        go.Bar(

            x=["Prediction"],

            y=[prediction],

            name="Prediction"

        )

    )

    fig.update_layout(

        barmode="group",

        height=420

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    # ======================================================
    # RETURN GAUGE
    # ======================================================

    st.subheader("📈 Expected Return Gauge")

    gauge = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=expected,

            title={"text": "Expected Return %"},

            gauge={

                "axis": {"range": [-5, 5]},

                "bar": {"color": "green"},

                "steps": [

                    {"range": [-5, -2], "color": "#ff4b4b"},

                    {"range": [-2, 2], "color": "#ffd54f"},

                    {"range": [2, 5], "color": "#00c853"}

                ]

            }

        )

    )

    gauge.update_layout(height=350)

    st.plotly_chart(

        gauge,

        use_container_width=True

    )

    # ======================================================
    # DETAILS
    # ======================================================

    st.subheader("📋 Prediction Details")

    st.dataframe(

    df,

    use_container_width=True,

    height=400

)