"""
Code illustrating how to read JSON files.
"""
import json

with open("../architecture/ships.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data)
    