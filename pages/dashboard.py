import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("Interactive Tableau Dashboard 📊")

st.markdown("""
Welcome to the data visualization hub! This application provides deep-dive analytics into 
NJ Transit and Amtrak rail operations. Explore the primary executive overview below, 
and use the tabs further down to read detailed deep-dives into line punctuality and station bottlenecks.
""")

# Engineering Context & Navigation Tips
with st.expander("ℹ️ **Engineering & Architecture Notes (Dataset & Layout)**", expanded=False):
    st.markdown("""
    * **Data Volume & Compute Limitation:** This dashboard aggregates **6 million+ rows** of operational data. Due to Tableau Public's browser-side compute boundaries on global aggregations, certain top-level total metrics may render as `0.0M`. Detailed route-level metrics, filtering, and geospatial maps remain fully functional.
    * **Display & Navigation:** To preserve the dense KPI layout without reflowing components, this view uses a fixed-width canvas sizing. **If viewing on a smaller screen, please scroll horizontally across the embedded frame to view the complete dashboard.**
    """)

st.markdown("---")
st.subheader("🔍 Deep-Dive Analysis & Insights")
st.markdown("Explore the detailed breakdowns below for each operational focus area corresponding to the dataset:")

# --- TABS FOR IN-DEPTH TEXT & METRIC BREAKDOWNS ---
tab1, tab2, tab3 = st.tabs([
    "Executive Overview Deep-Dive", 
    "Line Punctuality Breakdown", 
    "Station Risk & Bottlenecks Analysis"
])

with tab1:
    st.markdown("### Executive Operations Summary")
    st.write("""
    - **Global Volume:** Managing massive throughput derived from over 6 million aggregated records.
    - **Geospatial Spread:** Tracking trip density across multiple regional sectors in New Jersey and connecting transit corridors.
    - **Temporal Trends:** Hourly volume curves highlighting peak commuter rushes versus off-peak lulls.
    """)

with tab2:
    st.markdown("### Line Punctuality Analysis")
    st.write("""
    - **Reliability Metrics:** Assessing delay distributions across major active lines (e.g., NJ Coast Line, Northeast Corridor).
    - **Bottleneck Identification:** Pinpointing specific segments experiencing recurring schedule variances.
    - **Operational Impact:** How regional weather patterns and high-density scheduling compound delays.
    """)

with tab3:
    st.markdown("### Station Risk & Operational Bottlenecks")
    st.write("""
    - **High-Risk Hubs:** Analyzing congestion patterns at critical transfer stations like Hoboken and New York Penn Station.
    - **Platform Capacity:** Evaluating dwell times and passenger flow friction points during peak operating hours.
    - **Mitigation Insights:** Strategic takeaways for improving terminal throughput.
    """)

# Container CSS Override to maximize horizontal screen real estate
st.markdown("""
    <style>
    div[data-testid="stMainBlockContainer"] {
        max-width: 100% !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    </style>
""", unsafe_allow_html=True)

tableau_iframe = """
<div style="width: 100%; height: 100%; overflow: hidden; display: flex; justify-content: center;">
    <iframe src="https://public.tableau.com/views/nj_transit/NJTransitExecutiveOperationsOverview?:embed=yes&:showVizHome=no&:toolbar=yes" 
            width="2800px" 
            height="900px" 
            style="border:none; transform: scale(0.85); transform-origin: top center;">
    </iframe>
</div>
"""
components.html(tableau_iframe, height=900, width=1900, scrolling=True)
