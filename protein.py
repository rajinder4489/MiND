



from py2neo import Graph, Node, Relationship

# Connect to Neo4j database
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

def create_protein(name, organism):
    """Create a protein node"""
    protein = Node("Protein", name=name, organism=organism)
    graph.create(protein)
    return protein

def create_interaction(protein_a, protein_b, conditions, expression_level):
    """Create a relationship between two proteins"""
    interaction = Relationship(protein_a, "INTERACTS_WITH", protein_b, 
                               conditions=conditions, 
                               expression_level=expression_level)
    graph.create(interaction)

def protein_expression(protein_a, protein_b):
    """Define the expression of protein A to protein B"""
    import pandas as pd
    
    # Load the expression table
    expression_table = pd.read_csv('expression_data.csv', index_col='protein')
    
    # Get the expression level for protein_a in relation to protein_b
    try:
        expression_level = expression_table.loc[protein_a.name, protein_b.name]
        
        # Categorize the expression level
        if expression_level > 1.5:
            return "up-regulated"
        elif expression_level < 0.5:
            return "down-regulated"
        else:
            return "normal"
    except KeyError:
        # If the protein pair is not in the table, return 'unknown'
        return "unknown"

# Example usage
import csv

# Read protein interactions from a CSV file
with open('protein_interactions.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        protein_a = create_protein(row['protein_a'], row['organism_a'])
        protein_b = create_protein(row['protein_b'], row['organism_b'])
        
        conditions = row['conditions']
        expression = protein_expression(protein_a, protein_b)
        
        create_interaction(protein_a, protein_b, conditions, expression)

# Query example
result = graph.run("MATCH (p:Protein)-[r:INTERACTS_WITH]->(q:Protein) "
                   "RETURN p.name, r.conditions, r.expression_level, q.name").data()

for record in result:
    print(f"{record['p.name']} interacts with {record['q.name']} "
          f"under conditions: {record['r.conditions']} "
          f"with expression level: {record['r.expression_level']}")
