import pandas as pd
import requests

def fetch_dbsnp_data(rs_id):
    """Fetch data from dbSNP"""
    url = f"https://api.ncbi.nlm.nih.gov/variation/v0/refsnp/{rs_id}"
    response = requests.get(url)
    return response.json()

def save_dbsnp_data_to_csv():
    dbsnp_data = fetch_dbsnp_data("rs123")  # Example SNP ID
    df = pd.DataFrame([dbsnp_data])
    df.to_csv('dbsnp_data.csv', index=False)
    print("dbSNP data saved to dbsnp_data.csv")

if __name__ == "__main__":
    save_dbsnp_data_to_csv()