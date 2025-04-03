import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

def load_market_data(filepath):
    """
    Load and clean farmers market data from CSV.
    Automatically finds latitude, longitude, and name columns where possible.
    """
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
    df = df.dropna(subset=["lat", "lon"])
    if name_col:
        df = df.rename(columns={name_col: "name"})
    else:
        df["name"] = "Unknown Market"

    return df

def render_heatmap(df):
    """
    Render an interactive clustered heatmap of farmers market locations.
    Each dot represents a USDA-listed farmers market.
    Helps users visualize regional access to local food networks.
    """
    m = folium.Map(location=[39.5, -98.35], zoom_start=4, control_scale=True)
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

    # Contextual explanation for the user
    st.markdown("""
    #### 🗺️ What You’re Seeing
    This map uses data from the USDA Farmers Market Directory to show actual market locations across the United States.

    - Green circles represent markets where local foods are sold
    - Use this to identify high-density market areas or underserved regions
    - Producers can use this to explore potential new areas to sell or expand

    This view supports the core goal of FarmLinkIQ: making **local food systems more accessible and data-informed**.
    """)