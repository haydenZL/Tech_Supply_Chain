import streamlit as st
import pandas as pd
import json
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Global Tech Supply Chain Tracker", layout="wide")
st.title("🌐 Tech Supply Chain Entity & Risk Tracker")
st.markdown("Analysing semiconductor and hardware supply chain using scraped data.")

# 1. Coordinate Dictionary for Country Mapping
COUNTRY_COORDINATES = {
    "Taiwan": [23.6978, 120.9605],
    "China": [35.8617, 104.1954],
    "USA": [37.0902, -95.7129],
    "United States": [37.0902, -95.7129],
    "Japan": [36.2048, 138.2529],
    "South Korea": [35.9078, 127.7669],
    "Germany": [51.1657, 10.4515],
    "Netherlands": [52.1326, 5.2913],
}

# 2. Load the Standardized Data
@st.cache_data
def load_data():
    try:
        with open("standardised_entities.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

data = load_data()

if not data:
    st.error("No data found! Please run your extraction notebook to generate 'standardised_entities.json'.")
else:
    df = pd.DataFrame(data)

    # 3. Sidebar Filters
    st.sidebar.header("Filter Options")
    risk_filter = st.sidebar.multiselect(
        "Select Risk Levels to Display:",
        options=list(df['risk_level'].unique()),
        default=list(df['risk_level'].unique())
    )
    
    filtered_df = df[df['risk_level'].isin(risk_filter)]

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Tracked Entities", len(filtered_df))
    col2.metric("High Risk Scenarios", len(filtered_df[filtered_df['risk_level'] == 'High']))
    col3.metric("Primary Country Hubs", filtered_df['primary_country'].nunique())

    st.markdown("---")

    st.subheader("Map View: Geo-Impact of Tech Narratives")
    
    # Base map centered globally
    m = folium.Map(location=[25.0, 40.0], zoom_start=2, tiles="CartoDB positron")

    # Assign color to risk levels
    def get_risk_color(risk):
        if risk == "High": return "red"
        elif risk == "Medium": return "orange"
        return "green"

    # Plot each filtered article row onto the map
    for _, row in filtered_df.iterrows():
        country = row['primary_country']
        if country in COUNTRY_COORDINATES:
            coords = COUNTRY_COORDINATES[country]
            
            # Setup text popup when user clicks a map pin
            popup_html = f"""
            <strong>Company:</strong> {row['extracted_company']}<br>
            <strong>Sector:</strong> {row['technology_sector']}<br>
            <strong>Risk Level:</strong> <span style='color:{get_risk_color(row['risk_level'])}'><strong>{row['risk_level']}</strong></span><br>
            <a href='{row['url']}' target='_blank'>Read Original Article</a>
            """
            
            folium.Marker(
                location=coords,
                popup=folium.Popup(popup_html, max_width=300),
                tooltip=f"{row['extracted_company']} ({country})",
                icon=folium.Icon(color=get_risk_color(row['risk_level']), icon="info-sign")
            ).add_to(m)

    st_folium(m, width=1100, height=500)

    # 6. Setup raw data table below the map 
    st.markdown("---")
    st.subheader("Tabular View of Enriched Pipeline Data")
    st.dataframe(filtered_df, use_container_width=True)