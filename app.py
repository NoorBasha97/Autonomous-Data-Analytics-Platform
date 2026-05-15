# app.py

import streamlit as st
import pandas as pd

from graph.workflow import create_workflow
from main import initialize_state

st.set_page_config(page_title="AI Data Analytics", layout="wide")

st.title("📊 Autonomous Data Analytics Platform")

# 🔹 File Upload
uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

# 🔹 User Query
user_query = st.text_input("Ask a question about your data (optional)")

# 🔹 Analyze Button
if st.button("Analyze"):

    if uploaded_file is None:
        st.error("Please upload a file first.")
    else:
        with st.spinner("Analyzing data..."):

            # Save uploaded file temporarily
            file_path = f"temp_{uploaded_file.name}"
            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())

            # Initialize state
            state = initialize_state()
            state["file_path"] = file_path
            state["query"] = user_query if user_query else "General analysis"

            # Run workflow
            app = create_workflow()
            final_state = app.invoke(state)

        st.success("Analysis Completed!")

        # 🟢 DATA PREVIEW
        st.subheader("📄 Dataset Preview")
        if final_state.get("dataframe") is not None:
            st.dataframe(final_state["dataframe"].head())
        else:
            st.warning("No data available.")

        # 🟢 EDA SUMMARY
        st.subheader("📊 EDA Summary")
        st.write(final_state.get("eda_text", "No EDA available"))

        # 🟢 VISUALIZATIONS (IMPROVED UI)
        st.subheader("📈 Visualizations")

        plots = final_state.get("plots")

        if plots:
            cols = st.columns(2)  # 👈 2 plots per row

            for i, (col, plot_type, plot) in enumerate(plots):
                with cols[i % 2]:
                    st.markdown(f"**{col} ({plot_type})**")
                    st.pyplot(plot, use_container_width=False)
        else:
            st.warning(final_state.get("plot_status", "No plots available"))

        # 🟢 INSIGHTS
        st.subheader("🧠 Insights")

        insight_status = final_state.get("insight_status")

        if insight_status == "success":
            st.success(final_state["insights"])
        elif insight_status == "fallback":
            st.warning(final_state["insights"])
        else:
            st.info(final_state["insights"])