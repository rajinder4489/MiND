import pandas as pd
from neo4j import GraphDatabase

def add_to_neo4j():
    # Load merged data
    merged_data = pd.read_csv('merged_biological_data.csv')

    # Set up Neo4j client
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

    def store_in_neo4j(tx, gene_id, protein_id):
        tx.run("MERGE (g:Gene {id: $gene_id}) "
               "MERGE (p:Protein {id: $protein_id}) "
               "MERGE (g)-[:ENCODES]->(p)",
               gene_id=gene_id, protein_id=protein_id)

    with driver.session() as session:
        for index, row in merged_data.iterrows():
            session.write_transaction(store_in_neo4j, row['GeneID'], row['Entry'])

    print("Data added to Neo4j database.")

if __name__ == "__main__":
    add_to_neo4j()