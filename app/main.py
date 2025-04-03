import streamlit as st

st.set_page_config(page_title="FarmLinkIQ Prototype", layout="wide")

st.title("🌱 FarmLinkIQ Prototype")
st.subheader("Local Market Insights & Food Waste Estimator")

st.markdown("""
Welcome to **FarmLinkIQ** — a tool designed to help local farmers and food producers make smarter, more sustainable decisions. 

This prototype was built for the **MSBA 680: Big Data & Innovation** course at the University of Montana and focuses on helping producers:
- Discover local food market opportunities
- Estimate and reduce food waste
- Understand the environmental impact of their operations

Use the sidebar to explore each tool in the app.
""")

# Sidebar navigation
menu = st.sidebar.radio("Choose a tool:", ["🗺️ Market Heatmap", "🥕 Food Waste Estimator"])

if menu == "🗺️ Market Heatmap":
    st.header("🗺️ Local Food Market Heatmap")
    st.markdown("""
    This interactive map shows the locations of farmers markets across the U.S. using USDA data. 

    Each green dot represents a market where producers sell local food. Use the map to:
    - Discover where markets are concentrated
    - Identify regions with few markets (opportunities!)
    - Plan smarter distribution routes

    👉 **Tip:** Hover over a dot to see the market name. Zoom in to explore your area.
    """)

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
    st.markdown("""
    This tool helps producers estimate food waste and its environmental impact.

    Using USDA food loss data, we calculate:
    - How much food may be lost in the retail and consumer chain
    - How many pounds of food waste this produces
    - The equivalent CO₂ emissions from that waste

    👉 This helps small producers reduce waste, save money, and support sustainability.
    """)

    from waste_calculator import load_all_food_data, get_food_options, estimate_waste

    try:
        df = load_all_food_data()
        options_df = get_food_options(df)
        selected_name = st.selectbox("Select a food item", options_df["CleanName"].tolist())
        qty = st.slider("Enter quantity (lbs)", 1, 1000, 100)

        if st.button("Estimate Waste"):
            results = estimate_waste(df, selected_name, qty)

            if results:
                st.metric("Estimated Waste (lbs)", results["waste_lbs"])
                st.metric("Estimated CO₂ Emissions", f"{results['emissions_lbs']} lbs")
                st.metric("Total Loss Rate", f"{results['total_loss_pct']}%")

                with st.expander("🔍 Details"):
                    st.write(f"**Original Entry:** {results['original_name']}")
                    st.write(f"**Category:** {results['category']}")
                    st.caption(f"📁 Source File: {results['source_file']}")
            else:
                st.error("Could not find data for the selected item.")

    except Exception as e:
        st.error("There was a problem loading food data.")
        st.exception(e)