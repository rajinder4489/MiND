import pandas as pd
from bioservices import UniProt

def fetch_uniprot_data(query, limit=10):
    """Fetch data from UniProt"""
    uniprot = UniProt()
    result = uniprot.search(query, limit=limit)
    return [uniprot.retrieve(id) for id in result.split('\n') if id]

def save_uniprot_data_to_csv():
    protein_data = fetch_uniprot_data("organism:9606 AND reviewed:yes")
    df = pd.DataFrame(protein_data)
    df.to_csv('uniprot_proteins.csv', index=False)
    print("UniProt data saved to uniprot_proteins.csv")

if __name__ == "__main__":
    save_uniprot_data_to_csv()