import streamlit as st


def show():

    st.title("ℹ About Project")

    st.markdown("---")

    st.subheader("Nifty50 Data Engine")

    st.write("""
This is an end-to-end Machine Learning project for predicting Nifty50 stock prices.

### Features

- 📥 Data Downloader
- 🗄 SQLite Database
- 📊 Feature Engineering
- 🤖 Random Forest Model
- 📈 Market Scanner
- 📉 Model Evaluation
- 📄 Prediction Reports
- 🌐 Streamlit Dashboard

### Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Streamlit
- SQLite

### Author

Aamir
""")