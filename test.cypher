// Step 1: Create nodes
CREATE 
  // Proteins
  (p1:Protein {id: 'P1', name: 'Protein1'}),
  (p2:Protein {id: 'P2', name: 'Protein2'}),
  (p3:Protein {id: 'P3', name: 'Protein3'}),
  (p4:Protein {id: 'P4', name: 'Protein4'}),
  (p5:Protein {id: 'P5', name: 'Protein5'}),
  (p6:Protein {id: 'P6', name: 'Protein6'}),
  (p7:Protein {id: 'P7', name: 'Protein7'}),
  (p8:Protein {id: 'P8', name: 'Protein8'}),
  (p9:Protein {id: 'P9', name: 'Protein9'}),
  (p10:Protein {id: 'P10', name: 'Protein10'}),
  
  // miRNAs
  (m1:miRNA {id: 'miR1', name: 'miRNA1'}),
  (m2:miRNA {id: 'miR2', name: 'miRNA2'}),
  (m3:miRNA {id: 'miR3', name: 'miRNA3'}),
  (m4:miRNA {id: 'miR4', name: 'miRNA4'}),
  (m5:miRNA {id: 'miR5', name: 'miRNA5'}),
  
  // Drugs
  (d1:Drug {id: 'Drug1', name: 'Drug1'}),
  (d2:Drug {id: 'Drug2', name: 'Drug2'}),
  
  // Disease
  (dz1:Disease {id: 'Disease1', name: 'Disease1'});

// Step 2: Create relationships
CREATE 
  // Protein interactions
  (p1)-[:ACTIVATES {type: 'activation', confidence: 0.9}]->(p2),
  (p2)-[:BINDS {type: 'binding', confidence: 0.8}]->(p3),
  (p4)-[:INHIBITS {type: 'inhibition', confidence: 0.95}]->(p5),
  (p6)-[:PHOSPHORYLATES {type: 'phosphorylation', site: 'Serine-42'}]->(p7),
  (p8)-[:INTERACTS {type: 'generic'}]->(p9),
  (p10)-[:DEGRADES {type: 'degradation'}]->(p1),
  
  // miRNA to Protein interactions
  (m1)-[:SILENCES {type: 'silencing', confidence: 0.85}]->(p1),
  (m2)-[:REGULATES {type: 'regulation', confidence: 0.9}]->(p3),
  (m3)-[:SILENCES {type: 'silencing', confidence: 0.75}]->(p5),
  (m4)-[:REGULATES {type: 'regulation', confidence: 0.8}]->(p7),
  (m5)-[:SILENCES {type: 'silencing', confidence: 0.7}]->(p9),
  
  // Drug interactions
  (d1)-[:INHIBITS {type: 'drug-target', confidence: 0.95}]->(p4),
  (d2)-[:BINDS {type: 'drug-binding', confidence: 0.9}]->(p6),
  
  // Disease associations
  (dz1)-[:ASSOCIATED_WITH {type: 'disease-protein', confidence: 0.8}]->(p2),
  (dz1)-[:TARGETED_BY {type: 'disease-miRNA', confidence: 0.9}]->(m3),
  (dz1)-[:TREATED_BY {type: 'drug-disease', confidence: 0.95}]->(d1);

// Step 3: Optional queries to verify the graph
MATCH (n) RETURN n; // View all nodes
MATCH (n)-[r]->(m) RETURN n, r, m; // View all relationships
