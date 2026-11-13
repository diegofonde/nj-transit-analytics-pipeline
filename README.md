# 🚆 NJ Transit & Amtrak Operational Analytics Hub

An end-to-end data engineering and business intelligence application analyzing **6+ million operational rail records** across NJ Transit and Amtrak corridors. Built with a Databricks Medallion architecture, interactive Tableau Public dashboards, and a custom-styled Streamlit web interface.

🔗 **[Live Streamlit Application]([https://nj-transit-analytics-pipeline-u94setjspttwnrya2jfita.streamlit.app])** | 📊 **[Tableau Public Workbook]([https://nj-transit-analytics-pipeline-u94setjspttwnrya2jfita.streamlit.app])**

---

## 📋 Project Overview

Regional rail networks face complex scheduling, weather, and congestion bottlenecks. This project ingests raw historical transit logs, transforms them into analytics-ready tables, and surfaces actionable KPIs across three core operational views:

1. **Executive Operations Overview:** High-level system throughput, regional county trip density, and hourly commuter volume curves.
2. **Line Punctuality Analysis:** Route-by-route reliability tracking an overall **4.2-minute average delay**, a **19.0% severe delay (> 6 min) rate**, hourly delay heat maps, and sequential delay accumulation.
3. **Station Risk & Operational Bottlenecks:** Station efficiency scoring (**82.37 overall score**), a Trip Volume vs. Delay SLA risk matrix, and seasonal weather impact correlations (wind speed, temperature, precipitation).

---

## 🏗️ System Architecture

```text
[Raw Transit & Weather Logs (6M+ Rows)]
                  │
                  ▼
┌───────────────────────────────────┐
│   Databricks Medallion Pipeline   │
│  • Bronze: Raw ingestion          │
│  • Silver: Cleaning & joins       │
│  • Gold: Aggregated KPI views     │
└───────────────────────────────────┘
                  │
                  ▼
┌───────────────────────────────────┐
│      Tableau Public Dashboards    │
│  • Executive Overview             │
│  • Line Punctuality               │
│  • Station Risk & Bottlenecks     │
└───────────────────────────────────┘
                  │
                  ▼
┌───────────────────────────────────┐
│     Streamlit Web Application     │
│  • Custom CSS full-width embed    │
│  • Interactive user guides        │
│  • Metric & architecture docs     │
└───────────────────────────────────┘
```

---

## 🔮 Future Improvements & Roadmap

While the current deployment successfully processes and visualizes the full 6M+ row dataset, future iterations would focus on scalability, responsive UX, and predictive analytics:

* **Pre-Aggregated Gold Summary Tables:** Materialize dedicated, lightweight summary views in Databricks specifically for top-level global KPIs to eliminate Tableau Public's browser-side compute bottlenecks (resolving `0.0M` global rendering artifacts).
* **Responsive Mobile & Tablet Layouts:** Build device-specific Tableau dashboard layouts using Tableau's Device Designer so mobile and smaller-screen users can view KPIs natively without horizontal scrolling.
* **Predictive Delay Modeling:** Integrate a machine learning model (e.g., XGBoost or Random Forest trained on historical weather and schedule sequences) to forecast high-risk station delays before they occur.
* **Automated Data Refresh:** Transition from static historical snapshots to scheduled Databricks workflows or live API ingestion for real-time NJ Transit feed updates.
│  • Interactive user guides        │
│  • Metric & architecture docs     │
└───────────────────────────────────┘
