def fetch_chembl_data():
    url = "https://www.ebi.ac.uk/chembl/api/data/target"
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data['targets'])

def save_chembl_data():
    df = fetch_chembl_data()
    df.to_csv('chembl_data.csv', index=False)
    print("ChEMBL data saved.")

if __name__ == "__main__":
    save_chembl_data()