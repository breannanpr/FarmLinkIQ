# FarmLinkIQ
Big Data for Homegrown, Local Food and Livestock Market Matching.

## FarmLinkIQ Prototype

This is a prototype for **FarmLinkIQ**, a data-driven platform designed to help small and local food producers make smarter, more sustainable decisions using public agricultural data.

The prototype features two key tools:
1. **Local Food Market Heatmap**  
   Visualizes farmers market density across the U.S. using USDA geospatial data.

2. **Food Waste Estimator**  
   Allows farmers to estimate spoilage, environmental impact, and potential financial loss based on produce type and quantity.

---

## Project Purpose

This project was developed as part of the MSBA 680: Big Data & Innovation course at the University of Montana.  
It demonstrates how open data + simple AI logic can deliver **real-world insights** for food system innovation and sustainability.                  

---

## 🛠️ How to Run

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/FarmLinkIQ-Prototype.git
   cd FarmLinkIQ-Prototype

Set up a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install dependencies**
  ```bash
  Copy
  Edit
  pip install -r requirements.txt

4. **Download the USDA Farmers Market CSV**
  You can get it from this link and place it in the data/ folder (not included here due to size).

5. **Run the Streamlit app**
  ```bash
  Copy
  Edit
  streamlit run app/main.py

---

## Tech Stack
- Python
- Streamlit
- Pandas
- Folium (for mapping)
- USDA Open Data

---

## Data Sources
- USDA Farmers Market Directory
- USDA Food Waste Estimates

---

## Data Ethics & Stewardship
FarmLinkIQ is committed to:
- Using public data responsibly
- Respecting privacy and transparency
- Enabling equitable access to local food

---

## Future Work
- Add buyer-seller matching system
- Incorporate pricing recommendations
- Expand visualizations with real-time weather data

---

## License
This project is licensed under the MIT License.
