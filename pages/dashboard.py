import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("Interactive Tableau Dashboard 📊")

# Remove Streamlit's max-width restrictions and side padding
st.markdown("""
    <style>
    /* Force main block container to take 100% viewport width */
    div[data-testid="stMainBlockContainer"] {
        max-width: 100% !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Interactive Tableau Dashboard 📊")

tableau_iframe = """
<div style="width: 100%; height: 100%; overflow: hidden; display: flex; justify-content: center;">
    <iframe src="https://public.tableau.com/views/nj_transit/NJTransitExecutiveOperationsOverview?:embed=yes&:showVizHome=no&:toolbar=yes" 
            width="2800px" 
            height="900px" 
            style="border:none; transform: scale(0.85); transform-origin: top center;">
    </iframe>
</div>
"""

# Now you can expand the component width significantly (e.g., 1800 - 2000px)
components.html(tableau_iframe, height=900, width=1900, scrolling=False)

st.markdown("""
    Welcome to the data visualization hub! This page features an interactive Tableau dashboard hosted on Tableau Public. 
    The page features 3 main dashboards, 
""")