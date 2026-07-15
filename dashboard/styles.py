import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/* ==========================
   GLOBAL
========================== */

html, body, [class*="css"]{

    font-size:18px !important;

}

/* Main Content */

.block-container{

    max-width:95%;

    padding-top:2rem;

    padding-left:2rem;

    padding-right:2rem;

}

/* ==========================
   HEADINGS
========================== */

h1{

    font-size:44px !important;

    font-weight:700 !important;

}

h2{

    font-size:34px !important;

}

h3{

    font-size:28px !important;

}

h4{

    font-size:22px !important;

}

p{

    font-size:18px !important;

}

/* ==========================
   SIDEBAR
========================== */

section[data-testid="stSidebar"]{

    width:290px !important;

}

section[data-testid="stSidebar"] *{

    font-size:18px !important;

}

/* ==========================
   METRICS
========================== */

div[data-testid="metric-container"]{

    background:#1d2535;

    padding:22px;

    border-radius:14px;

    border:1px solid #333;

}

div[data-testid="metric-container"] label{

    font-size:18px !important;

    font-weight:600;

}

div[data-testid="metric-container"] div{

    font-size:34px !important;

    font-weight:bold;

}

/* ==========================
   TABLE
========================== */

thead tr th{

    font-size:18px !important;

}

tbody tr td{

    font-size:17px !important;

}

/* ==========================
   SELECTBOX
========================== */

.stSelectbox label{

    font-size:18px !important;

    font-weight:bold;

}

/* ==========================
   BUTTON
========================== */

button{

    font-size:18px !important;

}

/* ==========================
   ALERTS
========================== */

.stSuccess{

    font-size:18px !important;

}

.stWarning{

    font-size:18px !important;

}

.stError{

    font-size:18px !important;

}

/* ==========================
   DATAFRAME
========================== */

[data-testid="stDataFrame"]{

    font-size:17px !important;

}

/* ==========================
   EXPANDER
========================== */

.streamlit-expanderHeader{

    font-size:20px !important;

}

</style>
""",
        unsafe_allow_html=True,
    )