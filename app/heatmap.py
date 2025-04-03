import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import streamlit as st

def load_market_data(filepath):
    """Load and clean farmers market data from CSV."""
    df = pd.read_csv(filepath)

    possible_lat_cols = ["Y", "Latitude", "lat", "LAT", "location_1.latitude"]
    possible_lon_cols = ["X", "Longitude", "lon", "LON", "location_1.longitude"]
    possible_name_cols = ["MarketName", "name", "market_name"]

    lat_col = next((col for col in possible_lat_cols if col in df.columns), None)
    lon_col = next((col for col in possible_lon_cols if col in df.columns), None)
    name_col = next((col for col in possible_name_cols if col in df.columns), None)

    if not lat_col or not lon_col:
        raise ValueError("Latitude and longitude columns not found in CSV")

    df = df.rename(columns={lat_col: "lat", lon_col: "lon"})
    if name_col:
        df = df.rename(columns={name_col: "name"})
    else:
        df["name"] = "Unknown Market"

    df = df.dropna(subset=["lat", "lon"])
    return df

def render_heatmap(df):
    """Render an interactive clustered heatmap of farmers market locations."""
    st.markdown("""
    ### 📍 Market Heatmap Demo

    This map shows the locations of farmers markets across the U.S. using USDA public data.
    You’ll notice a high concentration of points in the **Eastern United States**.

    🧠 **Why?**  
    The USDA dataset we’re using contains more detailed information from that region. For Montana and other areas, 
    current publicly available data is limited. That’s why you’ll see fewer points in the West.

    ⚡ **What This Demonstrates:**  
    Even with sparse data, this tool shows the **potential** for regional analysis. With improved data collection, 
    this map could be used by producers to:
    - Discover underserved areas
    - Identify new market opportunities
    - Inform decisions about where to sell

    This heatmap is a **proof of concept** for future use in Montana and beyond.
    """)

    m = folium.Map(location=[39.5, -98.35], zoom_start=4)
    marker_cluster = MarkerCluster().add_to(m)

    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row["lat"], row["lon"]],
            radius=5,
            color='green',
            fill=True,
            fill_opacity=0.6,
            tooltip=row["name"]
        ).add_to(marker_cluster)

    folium_static(m)
