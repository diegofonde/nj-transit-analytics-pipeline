import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title = "NJ Transit Analysis", layout = "wide")

home_page = st.Page("pages/home.py", title = "Home", icon = "🏠", default = True)
structure_page = st.Page("pages/structure.py", title = "Structure", default = False)
dashboard_page = st.Page("pages/dashboard.py", title = "Interactive Dashboard", icon = "📊", default = False)

pg = st.navigation([home_page, structure_page ,dashboard_page])
pg.run()
