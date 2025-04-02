import streamlit as st

st.set_page_config(page_title="FarmLinkIQ Prototype", layout="wide")

st.title("🌱 FarmLinkIQ Prototype")
st.subheader("Local Market Insights & Food Waste Estimator")

st.markdown("""
Welcome to the **FarmLinkIQ** prototype.  
This tool uses USDA open data to help local producers make smarter, more sustainable decisions.
""")

# Sidebar navigation
menu = st.sidebar.radio("Choose a tool:", ["🗺️ Market Heatmap", "🥕 Food Waste Estimator"])

if menu == "🗺️ Market Heatmap":
    st.header("🗺️ Local Food Market Heatmap")
    
    from heatmap import load_market_data, render_heatmap

    data_file = "data/Farmers_Markets.csv"

    try:
        df = load_market_data(data_file)
        st.success(f"Loaded {len(df)} farmers market locations.")
        render_heatmap(df)
    except Exception as e:
        st.error("Failed to load map data. Make sure the CSV is in the data/ folder.")
        st.exception(e)

elif menu == "🥕 Food Waste Estimator":
    st.header("🥕 Food Waste Estimator")

    from waste_calculator import load_all_food_data, get_food_options, estimate_waste

    df = load_all_food_data()
    options_df = get_food_options(df)
    selected_name = st.selectbox("Select a food item", options_df["CleanName"].tolist())
    qty = st.slider("Enter quantity (lbs)", 1, 1000, 100)

    if st.button("Estimate Waste"):
        results = estimate_waste(df, selected_name, qty)

        if results:
            st.success(f"Estimated Waste: {results['waste_lbs']} lbs")
            st.success(f"Estimated Emissions: {results['emissions_lbs']} lbs CO₂e")
            st.info(f"Total Loss Rate: {results['total_loss_pct']}%")
            st.caption(f"📁 Source: {results['source_file']}")
        else:
            st.error("Could not find data for the selected item.")