from config import get_database


dbname = get_database()
print("Base de données :", dbname)

collection = dbname["arbres"]
print("Collection :", collection)

print("Nombre de documents :", collection.count_documents({}))

arbres = collection.aggregate([
        {
            "$group": {
                "_id": "$nom",
                "nb": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "nb": -1
            }
        },
        {
            "$limit": 5
        }
    ])
for arbre in arbres:
    print(arbre)

"""
réponses aux questions :

- Lister les 10 premiers arbres du Bois de Vincennes
    arbres = collection.find(
        {"commune": "MANTES-LA-JOLIE"},
        {"_id": 0, "nom": 1}
    ).sort("nom", 1).limit(10)


- Lister les arbres de plus de 20 m
    arbres = collection.find(
        {"hauteur": {"$gt": 20}},
        {"_id": 0, "nom": 1, "hauteur": 1}
    )

- Arbres dont le nom contient "Chêne"
    arbres = collection.distinct(
        "nom",
        {"nom": {"$regex": "Chêne"}}
    )
    arbres.sort()

- Les 10 arbres les plus hauts du bois de boulogne : 
    arbres = collection.find(
        {"commune": "BOIS DE BOULOGNE"},
        {"_id": 0, "nom": 1,"hauteur":1}
    ).sort("hauteur", -1).limit(10)

- Arbres avec circonférence connue et > 3 m
    arbres = collection.find(
        {"circonference": {"$ne": None, "$gt": 3}},
        {"_id": 0, "nom": 1, "circonference": 1, "commune": 1}
    ).sort("circonference", -1).limit(10)

- Nombre d'arbres par commune
    arbres = collection.aggregate([
        {
            "$group": {
            "_id": "$commune",
            "nb_arbres": {"$sum": 1}
            }
        }
    ])
- Les 5 espèces les plus représentées


- Les communes avec plus de 50 arbres
    arbres = collection.aggregate([
        {
            "$group": {
                "_id": "$commune",
                "nb_arbres": {"$sum": 1}
            }
        },
        {
            "$match": {
                "nb_arbres": {"$gt": 50}
            }
        },
        {
            "$sort": {
                "nb_arbres": -1
            }
        }
    ])



"""