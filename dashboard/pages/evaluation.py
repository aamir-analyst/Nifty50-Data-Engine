import streamlit as st
import pandas as pd

from config.config import REPORT_DIR


def show():

    st.title("📊 Model Evaluation")

    evaluation_dir = REPORT_DIR / "evaluation"

    metrics_file = evaluation_dir / "evaluation_metrics.csv"

    if not metrics_file.exists():

        st.error("Run python -m ml.evaluator")

        return

    metrics = pd.read_csv(metrics_file)

    values = dict(

        zip(

            metrics["Metric"],

            metrics["Value"]

        )

    )

    c1,c2,c3,c4 = st.columns(4)

    c1.metric("MAE",f"{values['MAE']:.2f}")

    c2.metric("RMSE",f"{values['RMSE']:.2f}")

    c3.metric("R²",f"{values['R2']:.4f}")

    c4.metric("MAPE",f"{values['MAPE']:.2f}%")

    st.divider()

    col1,col2 = st.columns(2)

    with col1:

        st.subheader("📈 Feature Importance")

        st.image(

            evaluation_dir/"feature_importance.png",

            use_container_width=True

        )

        st.subheader("📉 Residual Plot")

        st.image(

            evaluation_dir/"residual_plot.png",

            use_container_width=True

        )

    with col2:

        st.subheader("📊 Actual vs Predicted")

        st.image(

            evaluation_dir/"actual_vs_predicted.png",

            use_container_width=True

        )

        st.subheader("📈 Error Distribution")

        st.image(

            evaluation_dir/"error_distribution.png",

            use_container_width=True

        )