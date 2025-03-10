import pandas as pd
import requests

def fetch_ensembl_data(species="homo_sapiens"):
    """Fetch data from Ensembl"""
    url = f"https://rest.ensembl.org/lookup/symbol/{species}/?content-type=application/json"
    response = requests.get(url)
    return response.json()

def save_ensembl_data_to_csv():
    ensembl_data = fetch_ensembl_data()
    df = pd.DataFrame(ensembl_data)
    df.to_csv('ensembl_genes.csv', index=False)
    print("Ensembl data saved to ensembl_genes.csv")

if __name__ == "__main__":
    save_ensembl_data_to_csv()