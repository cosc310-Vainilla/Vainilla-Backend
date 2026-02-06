import pandas as pd

# Load all data from the CSV
def load_all():
    return pd.read_csv("backend/app/data/food_delivery.csv")

# Save data back to the CSV file
def save_all(dataframe):
    dataframe.to_csv("backend/app/data/food_delivery.csv", index=False)
