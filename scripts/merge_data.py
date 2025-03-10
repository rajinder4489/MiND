import pandas as pd

def merge_data():
    # Load data from CSV files
    ncbi_data = pd.read_csv('ncbi_genes.csv')
    uniprot_data = pd.read_csv('uniprot_proteins.csv')
    kegg_data = pd.read_csv('kegg_pathways.csv')
    reactome_data = pd.read_csv('reactome_data.csv')
    rnacentral_data = pd.read_csv('rnacentral_data.csv')
    ensembl_data = pd.read_csv('ensembl_genes.csv')
    omim_data = pd.read_csv('omim_data.csv')
    dbsnp_data = pd.read_csv('dbsnp_data.csv')

    # Merge data (this is a simplified example)
    merged_data = pd.merge(ncbi_data, uniprot_data, left_on='GeneID', right_on='Entry', how='outer')
    merged_data = pd.merge(merged_data, kegg_data, left_on='GeneID', right_on='Pathway', how='outer')
    merged_data = pd.merge(merged_data, reactome_data, left_on='GeneID', right_on='Pathway', how='outer')
    merged_data = pd.merge(merged_data, rnacentral_data, left_on='GeneID', right_on='rna_id', how='outer')
    merged_data = pd.merge(merged_data, ensembl_data, left_on='GeneID', right_on='id', how='outer')
    merged_data = pd.merge(merged_data, omim_data, left_on='GeneID', right_on='gene_id', how='outer')
    merged_data = pd.merge(merged_data, dbsnp_data, left_on='GeneID', right_on='rs_id', how='outer')

    # Save merged data to CSV
    merged_data.to_csv('merged_biological_data.csv', index=False)
    print("Merged data saved to merged_biological_data.csv")

if __name__ == "__main__":
    merge_data()



def merge_data2():
    dgidb = pd.read_csv('dgidb_data.csv')
    stitch = pd.read_csv('stitch_data.csv')
    biogrid = pd.read_csv('biogrid_data.csv')
    reactome = pd.read_csv('reactome_data.csv')
    chembl = pd.read_csv('chembl_data.csv')

    # Example merging logic (adjust based on actual data structure)
    merged_data = pd.merge(dgidb, stitch, on='common_column', how='outer')
    merged_data = pd.merge(merged_data, biogrid, on='common_column', how='outer')
    merged_data = pd.merge(merged_data, reactome, on='common_column', how='outer')
    merged_data = pd.merge(merged_data, chembl, on='common_column', how='outer')

    merged_data.to_csv('merged_drug_gene_protein_interactions.csv', index=False)
    print("Merged data saved.")

if __name__ == "__main__":
    merge_data2()