import streamlit as st


def sidebar():

    st.sidebar.image(
        "https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/python.svg",
        width=70
    )

    st.sidebar.title("Nifty50 AI")

    page = st.sidebar.radio(

        "Navigation",

        [

            "🏠 Home",

            "📈 Market",

            "🤖 Prediction",

            "📊 Evaluation",

            "📉 Charts",

            "📊 Live Analysis",

            "ℹ About"

        ]

    )

    st.sidebar.markdown("---")

    st.sidebar.success("Model : Random Forest")

    st.sidebar.info("Version : 3.0")

    return page