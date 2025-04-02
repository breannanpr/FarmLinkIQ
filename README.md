# 🌱 FarmLinkIQ Prototype

**FarmLinkIQ** is a lightweight, data-driven prototype designed to support local and small-scale agricultural producers. It helps farmers identify demand gaps, reduce food waste, and optimize their impact using publicly available datasets.

This project was developed as part of the **MSBA 680: Big Data & Innovation** course at the University of Montana. It showcases how open data and simple AI/analytics tools can empower producers and contribute to more sustainable food systems.

---

## 🚀 Features

### 🗺️ Local Food Market Heatmap
- Visualizes farmers market density across the U.S. using USDA geospatial data.
- Helps identify underserved regions and market opportunities.

### 🥕 Food Waste Estimator
- Calculates estimated food waste, CO₂ emissions, and financial loss based on product type and quantity.
- Pulls real waste rates from USDA datasets across multiple food groups:
  - Fruit
  - Vegetables
  - Meat, poultry, fish, eggs, and nuts
  - Grains
  - Dairy

---

## 📊 Data Sources

All datasets are provided by the U.S. Department of Agriculture (USDA):

- [USDA Farmers Market Directory](https://catalog.data.gov/dataset/farmers-markets)
- [USDA Food Availability (Per Capita) Data System](https://www.ers.usda.gov/data-products/food-availability-per-capita-data-system/), including:
  - [Fruit](https://www.ers.usda.gov/webdocs/DataFiles/47788/Fruit.csv)
  - [Vegetables](https://www.ers.usda.gov/webdocs/DataFiles/47788/Vegetables.csv)
  - [Grains](https://www.ers.usda.gov/webdocs/DataFiles/47788/Grain.csv)
  - [Meat, poultry, fish, eggs, and nuts](https://www.ers.usda.gov/webdocs/DataFiles/47788/Meat.csv)
  - [Dairy](https://www.ers.usda.gov/webdocs/DataFiles/47788/Dairy.csv)

> _Note: These datasets are stored locally in the `/data` directory and not included in the public repo due to file size._

---

## 🛠️ How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/breannanpr/FarmLinkIQ.git
   cd FarmLinkIQ
   ```

2. **Set up a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Place the USDA datasets**  
   Copy the following files into the `data/` folder:
   - `Farmers_Markets.csv`
   - `Fruit.csv`
   - `veg.csv`
   - `grain.csv`
   - `meat.csv`
   - `Dairy.csv`

5. **Run the Streamlit app**
   ```bash
   streamlit run app/main.py
   ```

---

## 🔐 Data Ethics & Stewardship

FarmLinkIQ is built on principles of responsible data use:
- Uses only public, government-provided datasets
- Promotes transparency, access, and equity
- Aims to improve sustainability through smart, data-informed agriculture

---

## 🧠 Future Work

This prototype could be expanded to include:
- AI-powered buyer/seller matching
- Real-time pricing optimization
- Integration with weather + satellite data
- Farmer or consumer login for customized insights

---

## 🙌 Acknowledgments

Special thanks to:
- Dr. Erik Guzik – for guidance in the MSBA 680 course
- USDA Economic Research Service – for high-quality, public datasets
- The open-source Python and Streamlit community

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).