import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

def load_market_data(filepath):
    """
    Loads USDA Farmers Market data from a CSV and returns a cleaned DataFrame
    with consistent latitude, longitude, and name columns.
    """
    df = pd.read_csv(filepath)

    # Try to detect possible column names for lat/lon/name
    possible_lat_cols = ["Y", "Latitude", "lat", "LAT", "location_1.latitude"]
    possible_lon_cols = ["X", "Longitude", "lon", "LON", "location_1.longitude"]
    possible_name_cols = ["MarketName", "name", "market_name"]

    lat_col = next((col for col in possible_lat_cols if col in df.columns), None)
    lon_col = next((col for col in possible_lon_cols if col in df.columns), None)
    name_col = next((col for col in possible_name_cols if col in df.columns), None)

    if not lat_col or not lon_col:
        raise ValueError("Latitude and longitude columns not found in CSV")

    df = df.rename(columns={lat_col: "lat", lon_col: "lon"})
    df["name"] = df[name_col] if name_col else "Unknown Market"
    df = df.dropna(subset=["lat", "lon"])

    return df

def render_heatmap(df):
    """
    Displays a Folium heatmap of farmers markets using clustering for readability.
    """
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