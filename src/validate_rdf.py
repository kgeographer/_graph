import os

from rdflib import Graph

cwd= os.getcwd()
g = Graph()
try:
    g.parse(cwd+"/lpo/lpo_draft_jul20240729b.ttl", format="ttl")
    print("The TTL file is valid.")
except Exception as e:
    print(f"An error occurred: {e}")