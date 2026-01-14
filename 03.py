from config import get_database


dbname = get_database()
print("Base de données :", dbname)

collection = dbname["arbres"]
print("Collection :", collection)

print("Nombre de documents :", collection.count_documents({}))

arbres = collection.find()
for arbre in arbres:
    print(arbre['_id'], arbre['nom'])




