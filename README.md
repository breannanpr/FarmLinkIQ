# 🌱 FarmLinkIQ Prototype

**FarmLinkIQ** is a lightweight, data-driven prototype designed to support local and small-scale agricultural producers. It helps farmers identify demand gaps, reduce food waste, and optimize their impact using publicly available datasets.

This project was developed as part of the **MSBA 680: Big Data & Innovation** course at the University of Montana. It showcases how open data and simple AI/analytics tools can empower producers and contribute to more sustainable food systems.

---

## 🚀 Features

### 🗺️ Local Food Market Heatmap
- Visualizes farmers market density across the U.S. using USDA geospatial data.
- Identifies underserved regions and local food market opportunities.
- Includes clustering and tooltips with market names for easier navigation.

### 🥕 Food Waste Estimator
- Calculates estimated food waste, CO₂ emissions, and financial loss based on product type and quantity.
- Uses real USDA loss rates across multiple food groups:
  - Fruit
  - Vegetables
  - Meat, poultry, fish, eggs, and nuts
  - Grains
  - Dairy
- Shows results with clear metrics and expandable detail views.

---

## 🌐 Live App Deployment

You can try the latest working version of FarmLinkIQ here:  
🔗 [https://farmlinkiq-xppy9zvww7dxzjprsoink6.streamlit.app/](https://farmlinkiq-xppy9zvww7dxzjprsoink6.streamlit.app/)

This link is hosted on **Streamlit Cloud** and reflects all real-time updates made via GitHub. No need to re-run scripts locally for testing or sharing!

---

## 📊 Data Sources

All datasets are provided by the U.S. Department of Agriculture (USDA):

- [USDA Farmers Market Directory](https://catalog.data.gov/dataset/farmers-markets)
- [USDA Food Availability (Per Capita) Data System](https://www.ers.usda.gov/data-products/food-availability-per-capita-data-system/), including:
  - Fruit.csv
  - veg.csv
  - grain.csv
  - meat.csv
  - Dairy.csv

> _Note: These datasets should be stored in the `data/` directory locally and are not included in the repo._

---

## 🧰 Project Structure

```plaintext
FarmLinkIQ/
├── app/
│   ├── main.py                # Streamlit entry point
│   ├── heatmap.py             # Heatmap logic and folium rendering
│   └── waste_calculator.py    # Food waste logic and calculator functions
├── data/                      # USDA food and market data CSVs
├── requirements.txt           # Python dependencies
├── README.md                  # Project overview
└── .gitignore
```

---

## 🛠️ How to Run the App (Windows / PowerShell)

### 1. Open PowerShell in the project folder:
```powershell
cd "C:\Users\breni\OneDrive\Documents\GitHub\FarmLinkIQ"
```

### 2. (Optional) Set up a virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install dependencies:
```powershell
pip install -r requirements.txt
```

### 4. Make sure your `data/` folder contains:
- Farmers_Markets.csv
- Fruit.csv
- veg.csv
- grain.csv
- meat.csv
- Dairy.csv

### 5. Launch the app:
```powershell
streamlit run main.py
```

---

## 🔐 Data Ethics & Stewardship

FarmLinkIQ is built on principles of responsible data use:
- Uses only public, government-provided datasets
- Promotes transparency, access, and equity
- Aims to improve sustainability through smart, data-informed agriculture
- No user data is collected or stored

---

## 🧠 Future Development Ideas

- AI-powered buyer/seller matching system
- Dynamic pricing analytics for local produce
- Real-time data integration from weather/satellite sources
- User login for personalized insights and dashboards
- Mobile-friendly UI and farmer outreach portal

---

## 🛠️ Code Fix for Food Waste Estimator

In `waste_calculator.py`, make sure `CleanName` is added immediately after data loading:

```python
combined_df = pd.concat(all_data, ignore_index=True)

# ✅ FIX: Add CleanName column so it's always available
temp_name = combined_df["Commodity"].fillna("")
combined_df["CleanName"] = temp_name.str.replace(r":.*$", "", regex=True).str.strip()

return combined_df
```

This ensures the dropdown and `estimate_waste()` logic won't break from a missing column.

---

## 🙌 Acknowledgments

Special thanks to:
- Dr. Erik Guzik – for guidance in MSBA 680
- USDA Economic Research Service – for high-quality, public datasets
- Open-source Python and Streamlit contributors

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
