import os
import pandas as pd
from Bio import Entrez

# Set up API keys and email for NCBI
Entrez.email = "your_email@example.com"
Entrez.api_key = "your_ncbi_api_key"

def fetch_ncbi_data(db, term, max_results=10):
    """Fetch data from NCBI databases"""
    handle = Entrez.esearch(db=db, term=term, retmax=max_results)
    record = Entrez.read(handle)
    id_list = record["IdList"]
    
    results = []
    for id in id_list:
        handle = Entrez.efetch(db=db, id=id, retmode="xml")
        results.append(Entrez.read(handle)[0])
    return results

def save_ncbi_data_to_csv():
    gene_data = fetch_ncbi_data("gene", "Homo sapiens[Organism] AND alive[prop]")
    df = pd.DataFrame(gene_data)
    df.to_csv('ncbi_genes.csv', index=False)
    print("NCBI data saved to ncbi_genes.csv")

if __name__ == "__main__":
    save_ncbi_data_to_csv()