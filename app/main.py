# Updated main.py without infinite launch loop
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

##streamlit run app/main.py
