import pandas as pd
from bioservices import Reactome

def fetch_reactome_data(query):
    """Fetch data from Reactome"""
    reactome = Reactome()
    return reactome.search_entity(query)

def save_reactome_data_to_csv():
    reactome_data = fetch_reactome_data("Homo sapiens")
    df = pd.DataFrame(reactome_data)
    df.to_csv('reactome_data.csv', index=False)
    print("Reactome data saved to reactome_data.csv")

if __name__ == "__main__":
    save_reactome_data_to_csv()