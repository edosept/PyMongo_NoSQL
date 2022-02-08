import pymongo as p
client = p.MongoClient('mongodb://localhost:27017/')

# Create a Database
mydb = client['databaseku']

# Create a Collection
mycol = mydb['collectionku']

# Inserting a Document
'''
To insert a document into a collection we can use the insert_one() method
'''
mydata = {'name': 'Abdul', 'usia': '21'}
x = mycol.insert_one(mydata)
x.inserted_id

mydata = {'name': 'Baba', 'usia': '19'}
x = mycol.insert_one(mydata)
x.inserted_id

mydata = {'name': 'Cici', 'usia': '20'}
x = mycol.insert_one(mydata)
x.inserted_id

# check databaseku, collectionku
print(client.list_database_names())
print(mydb.list_collection_names())

# ['admin', 'config', 'databaseku', 'local']
# ['collectionku']

# Find All Data as List
print(list(mycol.find()))
'''
[{'_id': ObjectId('614de9419edc6172cb2067c6'), 'name': 'Abdul', 'usia': '21'},
{'_id': ObjectId('614de94d9edc6172cb2067c7'), 'name': 'Baba', 'usia': '19'},
{'_id': ObjectId('614de9679edc6172cb2067c8'), 'name': 'Cici', 'usia': '20'}]
'''

# Find All Data
for x in mycol.find():
    print(x)
'''
{'_id': ObjectId('614de9419edc6172cb2067c6'), 'name': 'Abdul', 'usia': '21'}
{'_id': ObjectId('614de94d9edc6172cb2067c7'), 'name': 'Baba', 'usia': '19'}
{'_id': ObjectId('614de9679edc6172cb2067c8'), 'name': 'Cici', 'usia': '20'}
'''

# Find Data, name = 'Abdul'
mydoc = mycol.find({'name': 'Abdul'})

for x in mydoc:
    print(x)
'''
{'_id': ObjectId('614de9419edc6172cb2067c6'), 'name': 'Abdul', 'usia': '21'}
'''

# Delete by Data Property

# Print all data before delete
print(list(mycol.find()))
'''
[{'_id': ObjectId('614de9419edc6172cb2067c6'), 'name': 'Abdul', 'usia': '21'},
{'_id': ObjectId('614de94d9edc6172cb2067c7'), 'name': 'Baba', 'usia': '19'},
{'_id': ObjectId('614de9679edc6172cb2067c8'), 'name': 'Cici', 'usia': '20'}]
'''

# Delete by data property, 'name' = 'Abdul'
myquery = {'name': 'Abdul'}
mycol.delete_one(myquery)

# Print all data after delete
print(list(mycol.find()))
'''
[{'_id': ObjectId('614de94d9edc6172cb2067c7'), 'name': 'Baba', 'usia': '19'},
{'_id': ObjectId('614de9679edc6172cb2067c8'), 'name': 'Cici', 'usia': '20'}]
'''

# Update Data
# Print all data before update
print(list(mycol.find()))
'''
[{'_id': ObjectId('614de94d9edc6172cb2067c7'), 'name': 'Baba', 'usia': '19'},
{'_id': ObjectId('614de9679edc6172cb2067c8'), 'name': 'Cici', 'usia': '20'}]
'''

# Update data
myquery = {'name': 'Baba'}
newvalues = {'$set': {'name': 'Boni'}}
mycol.update_one(myquery, newvalues)

# Print all data after update
print(list(mycol.find()))
'''
[{'_id': ObjectId('614de94d9edc6172cb2067c7'), 'name': 'Boni', 'usia': '19'},
{'_id': ObjectId('614de9679edc6172cb2067c8'), 'name': 'Cici', 'usia': '20'}]
'''
