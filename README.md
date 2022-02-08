# PyMongo_NoSQL :clap:
*Using MongoDB With Python*
<br>

![PyMongo](https://files.realpython.com/media/Introduction-to-MongoDB-and-Python_Watermarked.a867c7233f3e.jpg)

<br>

# Overview

MongoDB works on concept of collection and document.

The following table shows the relationship of RDBMS terminology with MongoDB

![Overview](https://github.com/edosept/PyMongo_NoSQL/blob/main/Overview.png)

# PyMongo :leaves:
MongoDB provides an official Python driver called PyMongo :blush:

Before we start, make sure that you have the PyMongo distribution installed.

Python driver for MongoDB <http://www.mongodb.org>
>Installing PyMongo `pip install pymongo`

## Making a Connection with MongoClient
The first step when working with PyMongo is to create a MongoClient, to the running mongod instance

```
import pymongo as p
client = p.MongoClient('mongodb://localhost:27017/') # connect on the default host and port
# We can also specify the host and port explicitly
```

**let's write your python code with NoSQL** :grin:

# Source :book:
:file_folder:[pymongodocs](https://pymongo.readthedocs.io/en/stable/tutorial.html)

:file_folder:[tutorialspoint](https://www.tutorialspoint.com/mongodb/index.htm)

:file_folder:[realpython](https://realpython.com/introduction-to-mongodb-and-python/)
