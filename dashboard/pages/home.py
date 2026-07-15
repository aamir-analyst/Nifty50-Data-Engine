import streamlit as st
import pandas as pd
from datetime import datetime
from dashboard.components.cards import (
    info_card,
    success_card,
    warning_card,
    danger_card,
)
from dashboard.components.metrics import (
    show_kpi_cards,
    show_signal_cards,
)

from dashboard.utils.loader import (
    load_prediction_report,
)
from config.config import REPORT_DIR


def show():
    st.title("📈 Nifty50 AI Data Engine")

    st.caption("Machine Learning • Data Engineering • Stock Analytics")

    st.markdown("---")

    # ======================================================
    # LOAD DATA
    # ======================================================

    prediction_file = REPORT_DIR / "market_predictions.csv"
    df = load_prediction_report()

    if df is not None:
        buy = len(df[df["Signal"].str.contains("BUY")])
        hold = len(df[df["Signal"] == "HOLD"])
        sell = len(df[df["Signal"].str.contains("SELL")])
    else:
        buy = hold = sell = 0

    show_kpi_cards(
        50,
        23,
        "Random Forest",
        "99.96%"
    )

    show_signal_cards(
        buy,
        hold,
        sell
    )

    # ======================================================
    # KPI CARDS
    # ======================================================

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "📦 Stocks",
        "50"
    )

    c2.metric(
        "🧠 Features",
        "23"
    )

    c3.metric(
        "🤖 Model",
        "Random Forest"
    )

    c4.metric(
        "🎯 Accuracy",
        "99.96%"
    )

    st.markdown("---")

    # ======================================================
    # MARKET SUMMARY
    # ======================================================

    st.subheader("📊 Market Summary")

    a, b, c = st.columns(3)

    a.success(f"🟢 BUY\n\n{buy}")
    b.warning(f"🟡 HOLD\n\n{hold}")
    c.error(f"🔴 SELL\n\n{sell}")

    st.markdown("---")

    # ======================================================
    # PIPELINE STATUS
    # ======================================================

    st.subheader("⚙ Pipeline Status")

c1, c2 = st.columns(2)

with c1:
    success_card("Data Pipeline", "Completed")
    success_card("Feature Engineering", "Completed")
    success_card("Machine Learning", "Completed")

with c2:
    info_card("Database", "SQLite")
    info_card("Model", "Random Forest")
    info_card("Dashboard", "Streamlit")

    # ======================================================
    # LAST UPDATED
    # ======================================================

    st.info(f"Last Updated : {datetime.now().strftime('%d %B %Y %H:%M')}")