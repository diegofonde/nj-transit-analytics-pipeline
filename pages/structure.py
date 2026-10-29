import streamlit as st

st.title("Architecture🛠️")

st.image("images/architecture.png", caption="NJ Transit Data Engineering Pipeline", use_column_width=True)

st.markdown("---")

st.header("Pipeline Engineering & Data Transformation Strategy")
st.markdown("""
To ensure enterprise-grade reliability, data cleanliness, and analytical performance, the backend data pipeline is structured using a **Medallion Architecture** inside Databricks. This pattern progressively refines raw multi-source data into business-ready analytical models.
""")

# Use columns for a clean, side-by-side technical layout
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🥉 Bronze Layer")
    st.markdown("""
    **Raw Ingestion & Volume Storage**
    * Ingested historical operational logs from Kaggle directly into Databricks **Volumes**.
    * Fetched historical meteorological metrics via external **APIs** (Open-Meteo).
    * Generated foundational tables: `transit_trips`, `lines`, `stations`, and `weather`.
    """)

with col2:
    st.subheader("🥈 Silver Layer")
    st.markdown("""
    **Cleaning & Spatial Prep**
    * Standardized schemas, reconciling names between lines and stations.
    * Executed **environmental mapping** to link stations/lines to regional weather.
    * Performed **spatial transformations** (coordinate explosions) for map plotting.
    """)

with col3:
    st.subheader("🥇 Gold Layer")
    st.markdown("""
    **Modeling & Export**
    * Combined conformed `transit_trips` and `weather` with spatial tables.
    * Computed core risk metrics, delay timings, and the 6-minute SLA benchmark.
    * Saved final optimized tables as **CSVs back into Databricks Volumes** for Tableau.
    """)

st.markdown("---")

# Consumption Callout
st.info("""
📊 **Consumption Layer:** The finalized Gold-layer datasets are connected directly to **Tableau** to power executive dashboards, which are seamlessly embedded into this **Streamlit** web application via custom HTML iframes.
""")