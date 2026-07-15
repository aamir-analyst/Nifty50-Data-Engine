import streamlit as st
import pandas as pd
import plotly.express as px

from config.config import REPORT_DIR


def show():

    st.title("📈 AI Market Scanner")

    st.caption("Latest Machine Learning Predictions")

    st.markdown("---")

    prediction_file = REPORT_DIR / "market_predictions.csv"

    if not prediction_file.exists():

        st.error("Prediction report not found.")

        st.info("Run : python main.py --predict")

        return

    df = pd.read_csv(prediction_file)

    # ======================================================
    # KPI
    # ======================================================

    buy = len(df[df["Signal"].str.contains("BUY")])

    hold = len(df[df["Signal"] == "HOLD"])

    sell = len(df[df["Signal"].str.contains("SELL")])

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("🟢 BUY", buy)

    c2.metric("🟡 HOLD", hold)

    c3.metric("🔴 SELL", sell)

    c4.metric(
        "📦 Stocks",
        len(df)
    )

    st.markdown("---")

    # ======================================================
    # PIE CHART
    # ======================================================

    left, right = st.columns([1,2])

    with left:

        chart = (
            df.groupby("Signal")
            .size()
            .reset_index(name="Count")
        )

        fig = px.pie(

            chart,

            names="Signal",

            values="Count",

            hole=.55,

            title="Signal Distribution"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # ======================================================
    # BAR CHART
    # ======================================================

    with right:

        top10 = (
            df.sort_values(
                "Expected Return %",
                ascending=False
            )
            .head(10)
        )

        fig = px.bar(

            top10,

            x="Symbol",

            y="Expected Return %",

            color="Expected Return %",

            title="Top Expected Returns"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    st.markdown("---")

    # ======================================================
    # FILTERS
    # ======================================================

    c1, c2 = st.columns(2)

    with c1:

        signal = st.selectbox(

            "Signal",

            [

                "ALL",

                "BUY",

                "HOLD",

                "SELL"

            ]

        )

    with c2:

        stock = st.text_input(

            "Search Stock"

        )

    filtered = df.copy()

    if signal != "ALL":

        filtered = filtered[
            filtered["Signal"].str.contains(signal)
        ]

    if stock:

        filtered = filtered[
            filtered["Symbol"].str.contains(
                stock.upper()
            )
        ]

    st.markdown("---")

    # ======================================================
    # DOWNLOAD
    # ======================================================

    st.download_button(

        "⬇ Download Prediction Report",

        filtered.to_csv(index=False),

        "market_predictions.csv",

        "text/csv"

    )

    # ======================================================
    # TABLE
    # ======================================================

    st.dataframe(

    df,

    use_container_width=True,

    height=500

)