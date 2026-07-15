import streamlit as st

from dashboard.styles import load_css

from dashboard.components.sidebar import sidebar

from dashboard.pages.home import show as home
from dashboard.pages.market import show as market
from dashboard.pages.prediction import show as prediction
from dashboard.pages.evaluation import show as evaluation
from dashboard.pages.charts import show as charts
from dashboard.pages.about import show as about
from dashboard.pages.analysis import show as analysis

st.set_page_config(

    page_title="Nifty50 AI Dashboard",

    page_icon="📈",

   layout="wide",
initial_sidebar_state="expanded"

)

load_css()

page = sidebar()

if page == "🏠 Home":
    home()

elif page == "📈 Market":
    market()

elif page == "🤖 Prediction":
    prediction()

elif page == "📊 Evaluation":
    evaluation()

elif page == "📉 Charts":
    charts()

elif page == "📊 Live Analysis":
    analysis()

elif page == "ℹ About":
    about()