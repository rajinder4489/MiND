// Create nodes A and B
CREATE (a:Node {name: 'A'})
CREATE (b:Node {name: 'B'})

// Create relationships based on conditions
MATCH (a:Node {name: 'A'}), (b:Node {name: 'B'})
CREATE (a)-[:ACTIVATION {condition: 'C1'}]->(b)

MATCH (a:Node {name: 'A'}), (b:Node {name: 'B'})
CREATE (a)-[:DEGRADATION {condition: 'C2'}]->(b)

// Query to view the created structure
MATCH (a:Node {name: 'A'})-[r]->(b:Node {name: 'B'})
RETURN a, r, b