import pymongo as p
client = p.MongoClient('mongodb://localhost:27017/')

# Create a Database
mydb = client['databaseku']

# Create a Collection
mycol = mydb['collectionku']

# List of databases & collections
print(client.list_database_names())

print(mydb.list_collection_names())
