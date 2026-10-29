import streamlit as st

st.title("Home🏠")
st.header("Welcome to the home page!")

st.markdown("""
This web application is dedicated to showcasing the technical and analytical skills I have developed throughout my current position as a Pre-Sales Technical Engineer and in past roles.

### 🎯 Project Overview
Started on **October 23, 2026**, this project was designed and built within a single week to highlight enterprise-ready consulting capabilities. It analyzes NJ Transit system performance data spanning **2018–2020**, integrating multiple complex data sources:
* 📊 **Operational Logs:** Sourced from Pranav Badami's [NJ Transit + Amtrak (NEC) Rail Performance Dataset](https://www.kaggle.com/datasets/pranavbadami/nj-transit-amtrak-nec-performance) on Kaggle.
* 🗺️ **GIS & Spatial Data:** Sourced from the [NJGIN Open Data Center](https://njogis-newjersey.opendata.arcgis.com/search?groupIds=60a4f9a1342f4f7a94ac986e8dd14892&layout=grid).
* ⛅ **Meteorological Data:** Historical weather metrics fetched via [Open-Meteo](https://open-meteo.com/).

### ⚙️ Architecture & Processing
The data pipeline is engineered using a **Medallion Architecture** in Databricks for ingestion and cleaning, subsequently exporting the processed models into **Tableau** to build executive-level interactive reports.

### 🚀 Key Features & Navigation
1. **🛠️ Medallion Architecture:** An overview of the Databricks data pipeline structure and data engineering standards.
2. **📊 Station Vulnerability Dashboard:** High-impact data visualizations analyzing regional, line, and station-level risk matrices and weather correlations.
""")