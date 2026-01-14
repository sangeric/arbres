import requests
import json
import os

base_url = "https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/les-arbres/records"

output_dir = "data"
output_file = os.path.join(output_dir, "arbres_remarquables.json")

# Crée le dossier s'il n'existe pas
os.makedirs(output_dir, exist_ok=True)

all_results = []
limit = 100
offset = 0

while True:
    params = {
        "limit": limit,
        "offset": offset,
        "where": "remarquable='OUI'"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    results = data.get("results", [])
    if not results:
        break

    all_results.extend(results)
    offset += limit

# Sauvegarde dans data/
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_results, f, ensure_ascii=False, indent=2)

print(f"Fichier enregistré dans : {output_file}")
