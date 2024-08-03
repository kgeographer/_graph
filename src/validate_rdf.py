import os

from rdflib import Graph

filenames = ["/lpo/lpo_draft_jul20240729b.ttl",
             "/lpo/lpo_context.jsonld",
             "/data/vob10.jsonld",]
formats = ["ttl", "json-ld"]

cwd= os.getcwd()
g = Graph()
try:
    g.parse(cwd+filenames[0], format=formats[0])
    print("The TTL file is valid.")
except Exception as e:
    print(f"An error occurred: {e}")