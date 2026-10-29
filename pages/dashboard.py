import streamlit as st
import streamlit.components.v1 as components

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
<div style="width: 100%; overflow: hidden; display: flex; justify-content: center;">
    <iframe src="https://public.tableau.com/views/nj_transit/NJTransitExecutiveOperationsOverview?:embed=yes&:showVizHome=no&:toolbar=yes" 
            width="1200px" 
            height="850px" 
            style="border:none; transform: scale(0.85); transform-origin: 0 0;">
    </iframe>
</div>
"""

components.html(tableau_iframe,  height = 900, width = 1700, scrolling=False)

st.markdown("""
    Welcome to the data visualization hub! This page features an interactive Tableau dashboard hosted on Tableau Public. 
    The page features 3 main dashboards, 
""")