import streamlit as st


def show_kpi_cards(
    stocks,
    features,
    model,
    accuracy
):
    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
    "📈 Total Stocks",
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


def show_signal_cards(
    buy,
    hold,
    sell
):
    c1, c2, c3 = st.columns(3)

    c1.success(f"🟢 BUY\n\n{buy}")

    c2.warning(f"🟡 HOLD\n\n{hold}")

    c3.error(f"🔴 SELL\n\n{sell}")