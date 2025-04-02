import pandas as pd
import folium
from streamlit_folium import folium_static

def load_market_data(filepath):
    df = pd.read_csv(filepath)

    # Print to debug column names (optional)
    # print(df.columns)

    # Try multiple column names that USDA might use
    possible_lat_cols = ["Y", "Latitude", "lat", "LAT", "location_1.latitude"]
    possible_lon_cols = ["X", "Longitude", "lon", "LON", "location_1.longitude"]

    lat_col = next((col for col in possible_lat_cols if col in df.columns), None)
    lon_col = next((col for col in possible_lon_cols if col in df.columns), None)

    if not lat_col or not lon_col:
        raise ValueError("Latitude and longitude columns not found in CSV")

    df = df.rename(columns={lat_col: "lat", lon_col: "lon"})
    df = df.dropna(subset=["lat", "lon"])
    return df

def render_heatmap(df):
    m = folium.Map(location=[39.5, -98.35], zoom_start=4)

    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row["lat"], row["lon"]],
            radius=3,
            color='green',
            fill=True,
            fill_opacity=0.6
        ).add_to(m)

    folium_static(m)