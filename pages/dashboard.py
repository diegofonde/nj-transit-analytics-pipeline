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
<div class="tableau-container" style="width: 100%; display: flex; justify-content: center;">
    <iframe src="https://public.tableau.com/views/nj_transit/NJTransitExecutiveOperationsOverview?:embed=yes&:showVizHome=no&:toolbar=yes" 
            width="100%" 
            height="850px" 
            style="border:none; max-width: 100%;">
    </iframe>
</div>
"""

components.html(tableau_iframe,  height = 750, width = 1500, scrolling=False)

st.markdown("""
    Welcome to the data visualization hub! This page features an interactive Tableau dashboard hosted on Tableau Public. 
    The page features 3 main dashboards, 
""")