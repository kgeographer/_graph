import rdflib
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS

# Define namespaces
LPO = Namespace("https://example.org/lpo#")

# Initialize a Graph
g = Graph()

# Example Django-like data (replace with actual data query)
place_data = {
    "id": 1234,
    "name": ["Aberafan", "Aberavon"],
    "type": "InhabitedPlace"
}

# Create URIs for the subject (e.g., a place)
place_uri = URIRef(f"https://example.org/place/{place_data['id']}")

# Add triples to the graph
for name in place_data["name"]:
    g.add((place_uri, LPO.name, Literal(name)))

g.add((place_uri, RDF.type, LPO.Place))
g.add((place_uri, LPO.type, URIRef(LPO + place_data["type"])))

# Serialize to Turtle format
turtle_data = g.serialize(format="turtle", encoding="utf-8", indent=4)
print(turtle_data.decode("utf-8"))