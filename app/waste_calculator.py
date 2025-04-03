import pandas as pd
import os

def load_all_food_data(data_dir="data"):
    files = {
        "Fruit": "Fruit.csv",
        "Vegetables": "veg.csv",
        "Meat/Poultry/Fish": "meat.csv",
        "Grains": "grain.csv",
        "Dairy": "Dairy.csv"
    }

    all_data = []

    for category, filename in files.items():
        path = os.path.join(data_dir, filename)
        try:
            df = pd.read_csv(path)
            df["Category"] = category
            df["SourceFile"] = filename
            all_data.append(df)
        except Exception as e:
            print(f"Error loading {filename}: {e}")

    if not all_data:
        raise RuntimeError("No datasets could be loaded from the specified directory.")

    combined_df = pd.concat(all_data, ignore_index=True)

    # ✅ Ensure CleanName is always available
    combined_df["CleanName"] = combined_df["Commodity"].fillna("").str.replace(r":.*$", "", regex=True).str.strip()

    return combined_df

def get_food_options(df):
    return df[["CleanName", "Commodity"]].drop_duplicates().sort_values("CleanName")

def estimate_waste(df, selected_clean_name, quantity_lbs):
    match = df[df["CleanName"] == selected_clean_name]
    if match.empty:
        return None

    row = match.iloc[0]
    retail_loss = float(row.get("Retail loss", 0)) / 100
    consumer_loss = float(row.get("Consumer loss", 0)) / 100
    total_loss = retail_loss + consumer_loss

    EMISSIONS_PER_LB = 1.9
    waste_lbs = quantity_lbs * total_loss
    emissions_lbs = waste_lbs * EMISSIONS_PER_LB

    return {
        "waste_lbs": round(waste_lbs, 2),
        "emissions_lbs": round(emissions_lbs, 2),
        "total_loss_pct": round(total_loss * 100, 1),
        "source_file": row.get("SourceFile"),
        "category": row.get("Category"),
        "original_name": row.get("Commodity")
    }
