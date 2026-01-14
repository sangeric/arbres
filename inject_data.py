import json
from config import collection

with open("data/arbres.json", "r", encoding="utf-8") as f:
    arbres = json.load(f)

collection.delete_many({})

result = collection.insert_many(arbres)

print(f"{len(result.inserted_ids)} arbres insérés dans MongoDB")
