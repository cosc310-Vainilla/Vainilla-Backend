import pandas as pd
from typing import List, Dict, Any

DATA_PATH = "backend/app/data/food_delivery.csv"

def load_all() -> List[Dict[str, Any]]:
    try:
        data = pd.read_csv(DATA_PATH)
        return data.to_dict(orient='records')  # Convert DataFrame to list of dictionaries
    except FileNotFoundError:
        return []

def save_all(items: List[Dict[str, Any]]) -> None:
    df = pd.DataFrame(items)
    df.to_csv(DATA_PATH, index=False)
