"""
Code illustrating how to read JSON files.
"""
import json

with open("../architecture/ships.json", "r") as f:
    data = json.load(f)
    print(data)
    