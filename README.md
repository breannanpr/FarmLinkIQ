# 🌱 FarmLinkIQ Prototype

**FarmLinkIQ** is a lightweight, data-powered tool designed to support local and small-scale agricultural producers. It helps farmers answer key questions like:
- "Where are the best places to sell my food?"
- "How much of my produce might go to waste?"
- "What impact does food waste have on the environment?"

This prototype was built for the **MSBA 680: Big Data & Innovation** course at the University of Montana, showcasing how open data and simple analytics can empower real-world decision-making.

---

## 🧒 What Does FarmLinkIQ Do?

Imagine you're a farmer or food producer. You want to know two big things:
1. **Where should I sell my crops?**
2. **How can I reduce food waste and save money?**

FarmLinkIQ gives you smart answers by using real data from the U.S. government. It has two main tools:

---

## 🚀 Features

### 🗺️ 1. Local Food Market Heatmap

This interactive map helps farmers **see where farmers markets are** all over the United States.
- Every green dot = a local food market.
- Use this to find **hot spots** or **underserved areas**.
- Hover over dots to see market names. Zoom in to explore your region.

> 🧠 It's like a map that shows where you might make the most money.

---

### 🥕 2. Food Waste Estimator

This smart calculator helps you estimate how much food might be wasted — and how much pollution that causes.

- Select a food (like apples or cheese)
- Choose how much you’re growing (1 to 1000 lbs)
- Click "Estimate Waste"

It shows:
- **How many pounds are wasted**
- **CO₂ emissions caused by that waste**
- **Where the loss happens (retail or consumer side)**

> 🧠 This helps farmers waste less, save more, and protect the planet.

---

## 🌐 Live App Deployment

You can try the working version here:  
🔗 [https://farmlinkiq-xppy9zvww7dxzjprsoink6.streamlit.app/](https://farmlinkiq-xppy9zvww7dxzjprsoink6.streamlit.app/)

Built using [Streamlit](https://streamlit.io), it updates automatically when new changes are pushed to GitHub.

---

## 📊 Data Sources

FarmLinkIQ uses open data from the **U.S. Department of Agriculture (USDA)**:

- [USDA Farmers Market Directory](https://catalog.data.gov/dataset/farmers-markets)
- [USDA Food Availability Data](https://www.ers.usda.gov/data-products/food-availability-per-capita-data-system/), including:
  - Fruit.csv
  - veg.csv
  - grain.csv
  - meat.csv
  - Dairy.csv

> _Stored in the `data/` folder. Small sample files used for deployment._

---

## 🧰 Project Structure

```plaintext
FarmLinkIQ/
├── app/
│   ├── main.py                # Main app logic
│   ├── heatmap.py             # Interactive map code
│   └── waste_calculator.py    # Food waste analysis functions
├── data/                      # USDA sample data (CSV)
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Git exclusions
```

---

## 🛠️ How to Run the App (Locally)

### 1. Clone and open the project folder:
```powershell
cd FarmLinkIQ
```

### 2. Set up your environment:
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install the app dependencies:
```powershell
pip install -r requirements.txt
```

### 4. Ensure your `data/` folder contains:
- Farmers_Markets.csv
- Fruit.csv, veg.csv, grain.csv, meat.csv, Dairy.csv

### 5. Launch the app:
```powershell
streamlit run app/main.py
```

---

## 🔐 Data Ethics & Stewardship

FarmLinkIQ is guided by responsible data principles:
- Uses only public, open-source government data
- Does not collect any user data or personal info
- Promotes sustainability, food equity, and environmental awareness

---

## 🧠 Future Development Ideas

- AI-powered crop buyer matching system
- Real-time market pricing dashboard
- Climate/weather overlays on the map
- Personalized farm profiles with login
- Mobile-first design for farmer accessibility

---

## 🛠️ Code Fix: Food Estimator Stability

In `waste_calculator.py`, ensure the food name column (`CleanName`) is created:
```python
combined_df = pd.concat(all_data, ignore_index=True)
combined_df["CleanName"] = combined_df["Commodity"].fillna("").str.replace(r":.*$", "", regex=True).str.strip()
```
This ensures the dropdown works without crashing.

---

## 🙌 Acknowledgments

Huge thanks to:
- **Dr. Erik Guzik**
- **USDA Economic Research Service** 

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

Let’s build a better food future — one dataset at a time. 🌽📊
