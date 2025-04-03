import streamlit as st
from heatmap import load_market_data, render_heatmap
from waste_calculator import load_all_food_data, get_food_options, estimate_waste

st.set_page_config(page_title="FarmLinkIQ Prototype", layout="wide")
st.sidebar.title("Choose a page:")
page = st.sidebar.radio("", ["📘 Introduction", "🥕 Food Waste Estimator", "🗺️ Market Heatmap"])

# 1. Introduction
if page == "📘 Introduction":
    st.title("🌱 FarmLinkIQ Prototype")
    st.markdown("""
    Welcome to the **FarmLinkIQ** prototype — a data-driven tool built for small and regional food producers.

    Built for the **MSBA 680: Big Data & Innovation** course at the University of Montana, this project explores how 
    open data and analytics can help producers make better decisions, reduce waste, and expand market access.

    ---
    ### What This Prototype Shows:
    - How local market data can be visualized to identify underserved regions
    - How food loss can be estimated to reduce waste and greenhouse gas emissions
    - A framework for how small producers could use data to optimize their operations

    Use the sidebar to explore the tools!
    """)

# 2. Food Waste Estimator
elif page == "🥕 Food Waste Estimator":
    st.title("🥕 Food Waste Estimator")
    st.markdown("""
    This calculator helps producers estimate food waste and its environmental impact.

    Using USDA food loss data, we calculate:
    - 📦 Pounds of food waste based on item and quantity
    - 🌎 Associated CO₂ emissions (based on U.S. EPA estimates)
    - 📊 Total waste rate (retail + consumer)

    👉 This helps small producers reduce waste, save money, and support sustainability.
    """)

    try:
        df = load_all_food_data()
        food_options = get_food_options(df)

        selected_name = st.selectbox("Select a food item", food_options["CleanName"].tolist())
        qty = st.slider("Enter quantity (lbs)", min_value=1, max_value=1000, value=100)

        if st.button("Estimate Waste"):
            results = estimate_waste(df, selected_name, qty)
            if results:
                st.metric("Estimated Waste (lbs)", results["waste_lbs"])
                st.metric("Estimated CO₂ Emissions", f"{results['emissions_lbs']} lbs")
                st.metric("Total Loss Rate", f"{results['total_loss_pct']}%")

                with st.expander("🔍 Details"):
                    st.markdown(f"""
                    **Original Entry:** {results['original_name']}  
                    **Category:** {results['category']}  
                    🗂️ Source File: {results['source_file']}
                    """)
            else:
                st.warning("No data found for the selected item.")
    except Exception as e:
        st.error(f"Error loading food data: {e}")

# 3. Market Heatmap
elif page == "🗺️ Market Heatmap":
    st.title("🗺️ Local Food Market Heatmap")
    st.markdown("""
    This tool visualizes USDA Farmers Market locations across the U.S. to help producers identify market opportunities.

    ### Why This Matters:
    Understanding where markets are (and aren't) helps producers:
    - Identify underserved areas
    - Target new locations for selling products
    - Support local food access strategies

    ⚠️ Note: Current data includes mostly Eastern U.S. markets. This is a **proof of concept** — with more data, this can scale to Montana and beyond.
    """)

    try:
        data_file = "data/Farmers_Markets.csv"
        df = load_market_data(data_file)
        render_heatmap(df)
    except Exception as e:
        st.error(f"Failed to load map data. Please check that the CSV exists.\n\n{e}")