import pandas as pd
import requests

def fetch_rnacentral_data(query):
    """Fetch data from RNAcentral"""
    url = f"https://rnacentral.org/api/v1/rna?query={query}&format=json"
    response = requests.get(url)
    return response.json()

def save_rnacentral_data_to_csv():
    rna_data = fetch_rnacentral_data("species:\"Homo sapiens\"")
    df = pd.DataFrame(rna_data['results'])
    df.to_csv('rnacentral_data.csv', index=False)
    print("RNAcentral data saved to rnacentral_data.csv")

if __name__ == "__main__":
    save_rnacentral_data_to_csv()