# 🌱 FarmLinkIQ Prototype

**FarmLinkIQ** is a lightweight, data-driven prototype designed to support local and small-scale agricultural producers. It helps farmers identify demand gaps, reduce food waste, and optimize their impact using publicly available datasets.

This project was developed as part of the **MSBA 680: Big Data & Innovation** course at the University of Montana. It showcases how open data and simple AI/analytics tools can empower producers and contribute to more sustainable food systems.

---

## Features

### Local Food Market Heatmap
- Visualizes farmers market density across the U.S. using USDA geospatial data.
- Helps identify underserved regions and market opportunities.

### Food Waste Estimator
- Calculates estimated food waste, environmental impact, and potential financial loss based on user input.
- Uses USDA waste rates to simulate spoilage, CO₂ emissions, and economic value lost.

---

## Data Sources

- [USDA Farmers Market Directory (CSV)](https://catalog.data.gov/dataset/farmers-markets)
- [USDA Food Waste Estimates](https://www.ers.usda.gov/data-products/food-availability-per-capita-data-system/)

> _Note: These datasets are not included in the repository due to size. You'll need to download and add them manually._

---

## How to Run

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

4. **Download the USDA Farmers Market CSV**  
   You can download the dataset from the [USDA Farmers Market Directory](https://catalog.data.gov/dataset/farmers-markets)  
   and place it in the `data/` folder of this project.

   *(Note: The dataset is not included in the repo due to its size.)*

5. **Run the Streamlit app**
   ```bash
   streamlit run app/main.py
   ```

---

## Data Ethics & Stewardship

FarmLinkIQ is built on principles of responsible data use:
- Only public, freely available datasets are used.
- No personal or private data is collected or stored.
- The tool aims to improve **equity, sustainability, and access** in local food systems.

---

## Future Work

This prototype could be expanded to include:
- AI-driven buyer-seller matching
- Dynamic pricing recommendations
- User authentication and saved profiles
- Real-time weather and market alerts

---

## Acknowledgments

Special thanks to:
- Dr. Erik Guzik – for his guidance in the MSBA 680 course
- USDA and ERS for providing publicly available agricultural data
- Streamlit and open-source Python communities

---

## License

This project is licensed under the [MIT License](LICENSE).
