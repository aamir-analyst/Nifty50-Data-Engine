import streamlit as st


def info_card(title, value, icon="ℹ️"):

    st.markdown(
        f"""
        <div style="
            background:#1E293B;
            padding:20px;
            border-radius:15px;
            border:1px solid #334155;
            margin-bottom:15px;
            box-shadow:0 4px 10px rgba(0,0,0,0.25);
        ">
            <h4 style="margin:0;color:#CBD5E1;">{icon} {title}</h4>
            <h2 style="margin-top:10px;color:white;">{value}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


def success_card(title, value):

    st.markdown(
        f"""
        <div style="
            background:#052E16;
            padding:20px;
            border-radius:15px;
            border-left:6px solid #22C55E;
            margin-bottom:15px;
        ">
            <h4 style="margin:0;color:#86EFAC;">🟢 {title}</h4>
            <h2 style="color:white;">{value}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


def warning_card(title, value):

    st.markdown(
        f"""
        <div style="
            background:#451A03;
            padding:20px;
            border-radius:15px;
            border-left:6px solid #F59E0B;
            margin-bottom:15px;
        ">
            <h4 style="margin:0;color:#FCD34D;">🟡 {title}</h4>
            <h2 style="color:white;">{value}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


def danger_card(title, value):

    st.markdown(
        f"""
        <div style="
            background:#450A0A;
            padding:20px;
            border-radius:15px;
            border-left:6px solid #EF4444;
            margin-bottom:15px;
        ">
            <h4 style="margin:0;color:#FCA5A5;">🔴 {title}</h4>
            <h2 style="color:white;">{value}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )