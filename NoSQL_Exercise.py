# Make a Connection
import pymongo as p
client = p.MongoClient('mongodb://localhost:27017')

# Create Database and Collection
mydb = client['kampus-merdeka']
mycol = mydb['kelas-bigdata']

# Insert data
mydata = [
    {'Nama':'Joni', 'Domisili':'Jakarta', 'Hobi':'Coding'},
    {'Nama':'Levi', 'Domisili':'Bandung', 'Hobi':'Komunikasi'},
    {'Nama':'Erwin', 'Domisili':'Semarang', 'Hobi':'Bisnis'}
]

for i in mydata:
    x = mycol.insert_one(i)
    print(x.inserted_id)
'''
614f0b7d1d4d6c01b4b3178d
614f0b7e1d4d6c01b4b3178e
614f0b7e1d4d6c01b4b3178f
'''

for x in mycol.find():
    print(x)
'''
{'_id': ObjectId('614f0b7d1d4d6c01b4b3178d'), 'Nama': 'Joni', 'Domisili': 'Jakarta', 'Hobi': 'Coding'}
{'_id': ObjectId('614f0b7e1d4d6c01b4b3178e'), 'Nama': 'Levi', 'Domisili': 'Bandung', 'Hobi': 'Komunikasi'}
{'_id': ObjectId('614f0b7e1d4d6c01b4b3178f'), 'Nama': 'Erwin', 'Domisili': 'Semarang', 'Hobi': 'Bisnis'}
'''

# add two new data with properties “Nama”, “Usia”, “TinggiBadan”
mydata = [
    {'Nama': 'Armin','Usia':20, 'TinggiBadan':170},
    {'Nama': 'Mikasa','Usia': 25 , 'TinggiBadan': 190}
]

for i in mydata:
    x = mycol.insert_one(i)
    print(x.inserted_id)
'''
614f0b7e1d4d6c01b4b31790
614f0b7e1d4d6c01b4b31791
'''

for x in mycol.find():
    print(x)
'''
{'_id': ObjectId('614f0b7d1d4d6c01b4b3178d'), 'Nama': 'Joni', 'Domisili': 'Jakarta', 'Hobi': 'Coding'}
{'_id': ObjectId('614f0b7e1d4d6c01b4b3178e'), 'Nama': 'Levi', 'Domisili': 'Bandung', 'Hobi': 'Komunikasi'}
{'_id': ObjectId('614f0b7e1d4d6c01b4b3178f'), 'Nama': 'Erwin', 'Domisili': 'Semarang', 'Hobi': 'Bisnis'}
{'_id': ObjectId('614f0b7e1d4d6c01b4b31790'), 'Nama': 'Armin', 'Usia': 20, 'TinggiBadan': 170}
{'_id': ObjectId('614f0b7e1d4d6c01b4b31791'), 'Nama': 'Mikasa', 'Usia': 25, 'TinggiBadan': 190}
'''

# try to display only the last two data!
for x in mycol.find().skip(3):
    print(x)
'''
{'_id': ObjectId('614f0b7e1d4d6c01b4b31790'), 'Nama': 'Armin', 'Usia': 20, 'TinggiBadan': 170}
{'_id': ObjectId('614f0b7e1d4d6c01b4b31791'), 'Nama': 'Mikasa', 'Usia': 25, 'TinggiBadan': 190}
'''

# replace all field names that were originally "Nama" changed to "Identitas"
# Update data
myquery = {}
newvalues = {'$rename': {'Nama': 'Identitas'}}
mycol.update_many(myquery, newvalues)
'''
<pymongo.results.UpdateResult at 0x2517d9e74c0>
'''

for x in mycol.find():
    print(x)
'''
{'_id': ObjectId('614f0b7d1d4d6c01b4b3178d'), 'Domisili': 'Jakarta', 'Hobi': 'Coding', 'Identitas': 'Joni'}
{'_id': ObjectId('614f0b7e1d4d6c01b4b3178e'), 'Domisili': 'Bandung', 'Hobi': 'Komunikasi', 'Identitas': 'Levi'}
{'_id': ObjectId('614f0b7e1d4d6c01b4b3178f'), 'Domisili': 'Semarang', 'Hobi': 'Bisnis', 'Identitas': 'Erwin'}
{'_id': ObjectId('614f0b7e1d4d6c01b4b31790'), 'Usia': 20, 'TinggiBadan': 170, 'Identitas': 'Armin'}
{'_id': ObjectId('614f0b7e1d4d6c01b4b31791'), 'Usia': 25, 'TinggiBadan': 190, 'Identitas': 'Mikasa'}
'''

# show data that has TinggiBadan = 190 or Hobi = Coding!
mydoc =mycol.find({'$or': [{'TinggiBadan':190}, {'Hobi':'Coding'}]})

for x in mydoc:
    print(x)
'''
{'_id': ObjectId('614f0b7d1d4d6c01b4b3178d'), 'Domisili': 'Jakarta', 'Hobi': 'Coding', 'Identitas': 'Joni'}
{'_id': ObjectId('614f0b7e1d4d6c01b4b31791'), 'Usia': 25, 'TinggiBadan': 190, 'Identitas': 'Mikasa'}
'''

# display data sorted by "Identitas" in ascending order
for x in mycol.find().sort('Identitas', 1):
    print(x)
'''
{'_id': ObjectId('614f0b7e1d4d6c01b4b31790'), 'Usia': 20, 'TinggiBadan': 170, 'Identitas': 'Armin'}
{'_id': ObjectId('614f0b7e1d4d6c01b4b3178f'), 'Domisili': 'Semarang', 'Hobi': 'Bisnis', 'Identitas': 'Erwin'}
{'_id': ObjectId('614f0b7d1d4d6c01b4b3178d'), 'Domisili': 'Jakarta', 'Hobi': 'Coding', 'Identitas': 'Joni'}
{'_id': ObjectId('614f0b7e1d4d6c01b4b3178e'), 'Domisili': 'Bandung', 'Hobi': 'Komunikasi', 'Identitas': 'Levi'}
{'_id': ObjectId('614f0b7e1d4d6c01b4b31791'), 'Usia': 25, 'TinggiBadan': 190, 'Identitas': 'Mikasa'}
'''

# show data that has “Age” < 25
for x in mycol.find({'Usia': {'$lt': 25}}):
    print(x)
'''
{'_id': ObjectId('614f0b7e1d4d6c01b4b31790'), 'Usia': 20, 'TinggiBadan': 170, 'Identitas': 'Armin'}
'''

# display data that has an 'o' character in the middle of the character in the "Hobi" field or properties!
for x in mycol.find({'Hobi': {'$regex': 'o', '$options': 'a'}}):
    print(x)
'''
{'_id': ObjectId('614f0b7d1d4d6c01b4b3178d'), 'Domisili': 'Jakarta', 'Hobi': 'Coding', 'Identitas': 'Joni'}
{'_id': ObjectId('614f0b7e1d4d6c01b4b3178e'), 'Domisili': 'Bandung', 'Hobi': 'Komunikasi', 'Identitas': 'Levi'}
'''
