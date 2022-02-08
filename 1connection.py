# Making a Connection with MongoClient
'''
Before we start, make sure that you have the PyMongo distribution installed.

pip install pymongo

'''

'''
The first step when working with PyMongo is to create a MongoClient,
to the running mongod instance
'''

import pymongo as p
client = p.MongoClient('mongodb://localhost:27017/') # connect on the default host and port
# We can also specify the host and port explicitly
