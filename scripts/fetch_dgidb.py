import requests
import pandas as pd

def fetch_dgidb_data():
    url = "https://dgidb.org/api/v2/interactions.json"
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data['interactions'])

def save_dgidb_data():
    df = fetch_dgidb_data()
    df.to_csv('dgidb_data.csv', index=False)
    print("DGIdb data saved.")

if __name__ == "__main__":
    save_dgidb_data()