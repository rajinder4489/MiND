import pandas as pd
from bioservices import KEGG

def fetch_kegg_data(organism):
    """Fetch KEGG pathways for an organism"""
    kegg = KEGG()
    pathways = kegg.list("pathway", organism=organism)
    return {pathway: kegg.get(pathway) for pathway in pathways}

def save_kegg_data_to_csv():
    kegg_data = fetch_kegg_data("hsa")
    df = pd.DataFrame(list(kegg_data.items()), columns=['Pathway', 'Details'])
    df.to_csv('kegg_pathways.csv', index=False)
    print("KEGG data saved to kegg_pathways.csv")

if __name__ == "__main__":
    save_kegg_data_to_csv()