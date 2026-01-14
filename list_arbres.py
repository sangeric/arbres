from config import collection

arbres = collection.find()

for arbre in arbres:
    print(
        f"{arbre['libellefrancais']} "
        f"({arbre['genre']} {arbre['espece']}) - "
        f"{arbre['arrondissement']}"
    )
