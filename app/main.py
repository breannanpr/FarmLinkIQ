import streamlit as st
from app.heatmap import load_market_data, render_heatmap
from app.waste_calculator import load_all_food_data, get_food_options, estimate_waste

# Sidebar Navigation
st.set_page_config(page_title="FarmLinkIQ Prototype", layout="wide")
st.sidebar.title("Choose a page:")
page = st.sidebar.radio("", ["📘 Introduction", "🥕 Food Waste Estimator", "🗺️ Market Heatmap"])

# 1. Introduction Page
if page == "📘 Introduction":
    st.title("🌱 FarmLinkIQ Prototype")
    st.markdown("""
    Welcome to the **FarmLinkIQ** prototype — a data-driven tool created to support smarter, more sustainable decisions 
    for small and regional agricultural producers.

    ### 🎯 What This Project Does
    This prototype demonstrates how open USDA datasets can help producers:
    - 📍 Discover food market gaps
    - ❌ Estimate food waste and reduce environmental impact
    - 🧠 Make better decisions about where and how to distribute food

    Built for the **MSBA 680: Big Data & Innovation** course at the University of Montana, this tool is designed to explore 
    how data and AI tools can transform local food systems for the better.

    Use the **sidebar** to explore each of the tools in the prototype.
    """)

# 2. Food Waste Estimator
elif page == "🥕 Food Waste Estimator":
    st.title("🥕 Food Waste Estimator")
    st.markdown("""
    This calculator helps small producers and food system planners estimate how much food **might go to waste** before it reaches the consumer.

    ### 🧠 Why This Matters
    Food loss means lost revenue, avoidable environmental impact, and inefficiency. Understanding this allows producers to:
    - Adjust production based on loss rates
    - Estimate the hidden costs of waste
    - Reduce greenhouse gas emissions from overproduction

    This tool uses USDA food availability and loss data to estimate:
    - 📦 Pounds of food waste per item
    - 🌍 CO₂ emissions associated with that waste
    - 📊 Total loss rates (retail + consumer)

    ---
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
        st.error(f"There was a problem loading food data.\n\n{e}")

# 3. Market Heatmap Page
elif page == "🗺️ Market Heatmap":
    st.title("🗺️ Local Food Market Heatmap")

    st.markdown("""
    This interactive map visualizes USDA-registered farmers market locations across the United States.

    ### 🧠 How to Use This
    Identifying where markets are **concentrated vs. absent** can help:
    - 🧭 Allocate local food resources more effectively
    - 📍 Discover gaps in local food access
    - 🛒 Identify underserved areas that could benefit from new food hubs or producers

    🧪 This tool is a **prototype** — current USDA datasets contain more detailed info in the Eastern U.S.
    but this concept is designed to scale with better data (like for Montana or other rural areas).

    Future versions could dynamically highlight regions of opportunity based on food need and access levels.

    ---
    """)

    try:
        data_file = "data/Farmers_Markets.csv"
        df = load_market_data(data_file)
        render_heatmap(df)
    except Exception as e:
        st.error(f"Failed to load map data. Make sure the CSV is in the `data/` folder.\n\n{e}")