import streamlit as st

st.set_page_config(page_title="FarmLinkIQ", layout="wide")

# Sidebar navigation
menu = st.sidebar.radio("🔎 Choose a page:", ["📘 Introduction", "🥕 Food Waste Estimator", "🗺️ Market Heatmap"])

if menu == "📘 Introduction":
    st.title("🌱 Welcome to FarmLinkIQ")
    st.markdown("""
    **FarmLinkIQ** is a lightweight, data-powered prototype designed to help local and small-scale agricultural producers 
    make smarter, more sustainable decisions.

    This project was developed for **MSBA 680: Big Data & Innovation** at the University of Montana.

    ### 💡 What Can You Do Here?
    - Explore **food waste estimates** based on USDA data
    - Visualize **farmers market distribution** using real geospatial data
    - Discover how open data can support more sustainable, localized food systems

    This tool is not just about analysis — it's about showing what's possible when small producers have access to useful, visual insights.
    """)

elif menu == "🥕 Food Waste Estimator":
    st.header("🥕 Food Waste Estimator")
    st.markdown("""
    This calculator helps you understand how much food might go to waste and what that means for the environment.

    Using USDA-provided food loss data, we estimate:
    - The pounds of food waste for a selected item and quantity
    - The resulting CO₂ emissions
    - Total waste rate percentages

    👉 A simple way to see how smarter production can reduce waste and improve sustainability.
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

elif menu == "🗺️ Market Heatmap":
    st.header("🗺️ Local Market Heatmap (Prototype)")
    st.markdown("""
    This is a demonstration of what's possible with geospatial market data.

    🔍 While our dataset currently focuses on **East Coast markets** from a USDA sample, this tool shows how we could:
    - Visualize market density and underserved regions
    - Help farmers make informed choices on where to sell their goods
    - Highlight gaps in local food infrastructure

    ⚠️ Due to limited open data in Montana, this version demonstrates future potential using publicly available examples.
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