import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("Interactive Tableau Dashboard 📊")

# Make the Streamlit container use full width
st.markdown("""
    <style>
    .tableau-container {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Custom responsive iframe code
tableau_iframe = """
<div style="width: 100%; height: 100%; overflow: hidden; display: flex; justify-content: center;">
    <iframe src="https://public.tableau.com/views/nj_transit/NJTransitExecutiveOperationsOverview?:embed=yes&:showVizHome=no&:toolbar=yes" 
            width="2400px" 
            height="900px" 
            style="border:none; transform: scale(0.82); transform-origin: top center;">
    </iframe>
</div>
"""

# Increase this width integer to stretch it further across your screen
components.html(tableau_iframe, height=900, width=2000, scrolling=False)

st.markdown("""
    Welcome to the data visualization hub! This page features an interactive Tableau dashboard hosted on Tableau Public. 
    The page features 3 main dashboards, 
""")