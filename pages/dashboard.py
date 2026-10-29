import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("Interactive Tableau Dashboard 📊")

st.markdown("""
Welcome to the data visualization hub! This application provides deep-dive analytics into 
NJ Transit and Amtrak rail operations. Explore high-level executive performance, individual line punctuality, 
and critical station bottleneck risks across the three specialized dashboards below.
""")

# Engineering Context & Navigation Tips
with st.expander("ℹ️ **Engineering & Architecture Notes (Dataset & Layout)**", expanded=False):
    st.markdown("""
    * **Data Volume & Compute Limitation:** This dashboard aggregates **6 million+ rows** of operational data. Due to Tableau Public's browser-side compute boundaries on global aggregations, certain top-level total metrics may render as `0.0M`. Detailed route-level metrics, filtering, and geospatial maps remain fully functional.
    * **Display & Navigation:** To preserve the dense KPI layout without reflowing components, these embedded views use fixed-width canvas sizing. **If viewing on a smaller screen, please scroll horizontally across the embedded frame to view the complete dashboard.**
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

# Define Tabs
tab1, tab2, tab3 = st.tabs([
    "NJ Transit Executive Operations Overview", 
    "Line Punctuality", 
    "Station Risk & Operational Bottlenecks"
])

# --- TAB 1: Executive Overview ---
with tab1:
    st.subheader("Executive Operations Overview")
    st.caption("High-level system metrics, active line counts, regional trip volume maps, and hourly travel trends.")
    
    iframe_tab1 = """
    <div style="width: 100%; height: 100%; overflow: hidden; display: flex; justify-content: center;">
        <iframe src="https://public.tableau.com/views/nj_transit/NJTransitExecutiveOperationsOverview?:embed=yes&:showVizHome=no&:toolbar=yes" 
                width="2800px" 
                height="900px" 
                style="border:none; transform: scale(0.85); transform-origin: top center;">
        </iframe>
    </div>
    """
    components.html(iframe_tab1, height=900, width=1900, scrolling=True)

# --- TAB 2: Line Punctuality ---
with tab2:
    st.subheader("Line Punctuality & Delay Analysis")
    st.caption("On-time performance breakdown, route-by-route delays, and peak vs. off-peak reliability statistics.")
    
    # Replace the URL src below with your specific Tableau view URL for Line Punctuality
    iframe_tab2 = """
    <div style="width: 100%; height: 100%; overflow: hidden; display: flex; justify-content: center;">
        <iframe src="https://public.tableau.com/views/nj_transit/LinePunctuality?:embed=yes&:showVizHome=no&:toolbar=yes" 
                width="2800px" 
                height="900px" 
                style="border:none; transform: scale(0.85); transform-origin: top center;">
        </iframe>
    </div>
    """
    components.html(iframe_tab2, height=900, width=1900, scrolling=True)

# --- TAB 3: Station Risk & Bottlenecks ---
with tab3:
    st.subheader("Station Risk & Operational Bottlenecks")
    st.caption("Station congestion scoring, platform capacity constraints, and critical bottleneck identification.")
    
    # Replace the URL src below with your specific Tableau view URL for Station Risk
    iframe_tab3 = """
    <div style="width: 100%; height: 100%; overflow: hidden; display: flex; justify-content: center;">
        <iframe src="https://public.tableau.com/views/nj_transit/StationRiskOperationalBottlenecks?:embed=yes&:showVizHome=no&:toolbar=yes" 
                width="2800px" 
                height="900px" 
                style="border:none; transform: scale(0.85); transform-origin: top center;">
        </iframe>
    </div>
    """
    components.html(iframe_tab3, height=900, width=1900, scrolling=True)